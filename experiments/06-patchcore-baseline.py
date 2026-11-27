
from pathlib import Path

import anomalib
import torch

from anomalib.data import MVTecAD
from anomalib.engine import Engine
from anomalib.models import Patchcore


# ============================================================
# 1. CONFIGURATION
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_ROOT = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "mvtec-ad-metal-nut"
)

OUTPUT_DIR = PROJECT_ROOT / "results" / "patchcore"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# 2. ENVIRONMENT
# ============================================================

print("=== ENVIRONMENT ===")

print("Anomalib:", anomalib.__version__)
print("PyTorch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())


# ============================================================
# 3. DATA MODULE
# ============================================================

print("\n=== DATA MODULE ===")

datamodule = MVTecAD(
    root=str(DATASET_ROOT),
    category="metal_nut",
    train_batch_size=4,
    eval_batch_size=4,
    num_workers=0,
)

datamodule.setup()

print("Training images:", len(datamodule.train_data))
print("Test images:", len(datamodule.test_data))


# ============================================================
# 4. PATCHCORE MODEL
# ============================================================

print("\n=== MODEL CONFIGURATION ===")

model = Patchcore(
    backbone="resnet18",
    layers=["layer2", "layer3"],
    pre_trained=True,
    coreset_sampling_ratio=0.1,
    num_neighbors=9,
    precision="float32",
)

print("Model:", model.__class__.__name__)
print("Backbone: resnet18")
print("Layers: layer2, layer3")
print("Coreset sampling ratio: 0.1")


# ============================================================
# 5. ENGINE
# ============================================================

print("\n=== ENGINE SETUP ===")

engine = Engine(
    accelerator="cpu",
    devices=1,
    max_epochs=1,
    default_root_dir=str(OUTPUT_DIR),
)


# ============================================================
# 6. TRAINING
# ============================================================

print("\n=== TRAINING ===")

engine.fit(
    model=model,
    datamodule=datamodule,
)

print("Training completed!")


# ============================================================
# 7. EVALUATION
# ============================================================

print("\n=== EVALUATION ===")

test_results = engine.test(
    model=model,
    datamodule=datamodule,
)

print("\nEvaluation results:")

for result in test_results:
    print(result)


# ============================================================
# 8. SUMMARY
# ============================================================

print("\n=== BASELINE SUMMARY ===")

print("Model: PatchCore")
print("Dataset: MVTec AD - Metal Nut")
print("Training samples: 220 normal images")
print("Test samples: 115 images")
print("Execution device: CPU")

print("\nBaseline execution completed!")
