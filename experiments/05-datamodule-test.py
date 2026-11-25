
from pathlib import Path

import torch
from anomalib.data import MVTecAD

# ============================================================
# 1. CONFIGURAÇÕES
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_ROOT = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "mvtec-ad-metal-nut"
)

METAL_NUT_DIR = DATASET_ROOT / "metal_nut"

TRAIN_DIR = METAL_NUT_DIR / "train" / "good"
TEST_DIR = METAL_NUT_DIR / "test"
GROUND_TRUTH_DIR = METAL_NUT_DIR / "ground_truth"

# ============================================================
# 2. VALIDAR ESTRUTURA DO DATASET
# ============================================================

print("=== DATASET VALIDATION ===")

required_dirs = [
    TRAIN_DIR,
    TEST_DIR,
    GROUND_TRUTH_DIR,
]

for directory in required_dirs:
    if not directory.exists():
        raise FileNotFoundError(
            f"Diretório não encontrado: {directory}"
        )

train_images = list(TRAIN_DIR.glob("*.png"))

print(f"Imagens de treinamento: {len(train_images)}")

if len(train_images) == 0:
    raise RuntimeError(
        "Nenhuma imagem encontrada em train/good. "
        "Verifique se as imagens de treinamento foram baixadas."
    )

if len(train_images) != 220:
    print(
        f"AVISO: esperávamos 220 imagens, "
        f"mas encontramos {len(train_images)}."
    )

# ============================================================
# 3. CONFIGURAR DATAMODULE
# ============================================================

print("\n=== DATAMODULE SETUP ===")

datamodule = MVTecAD(
    root=str(DATASET_ROOT),
    category="metal_nut",
    train_batch_size=4,
    eval_batch_size=4,
    num_workers=0,
)

datamodule.setup()

# ============================================================
# 4. TESTAR TREINAMENTO
# ============================================================

print("\n=== TRAINING ===")

train_loader = datamodule.train_dataloader()

print("Quantidade de batches:", len(train_loader))

train_batch = next(iter(train_loader))

print("Formato das imagens:", train_batch.image.shape)
print("Formato dos labels:", train_batch.gt_label.shape)
print("Labels:", train_batch.gt_label.tolist())

# ============================================================
# 5. TESTAR TESTE
# ============================================================

print("\n=== TEST ===")

test_loader = datamodule.test_dataloader()

print("Quantidade de batches:", len(test_loader))

test_batch = next(iter(test_loader))

print("Formato das imagens:", test_batch.image.shape)
print("Formato dos labels:", test_batch.gt_label.shape)
print("Formato das máscaras:", test_batch.gt_mask.shape)

print(
    "Valores únicos das máscaras:",
    torch.unique(test_batch.gt_mask)
)

# ============================================================
# 6. RESUMO
# ============================================================

print("\n=== ENVIRONMENT ===")

print("PyTorch:", torch.__version__)
print("CUDA disponível:", torch.cuda.is_available())

print("\nTeste de integração concluído!")
