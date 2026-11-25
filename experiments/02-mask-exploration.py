from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_ROOT = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "mvtec-ad-metal-nut"
    / "metal_nut"
)

GROUND_TRUTH_DIR = DATASET_ROOT / "ground_truth"

print("Dataset:", DATASET_ROOT)
print("Ground truth existe:", GROUND_TRUTH_DIR.exists())

if GROUND_TRUTH_DIR.exists():
    for defect_dir in sorted(GROUND_TRUTH_DIR.iterdir()):
        if defect_dir.is_dir():
            masks = list(defect_dir.glob("*.png"))

            print(
                f"{defect_dir.name}: "
                f"{len(masks)} máscaras"
            )

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def inspect_mask(mask_path):
    mask = Image.open(mask_path).convert("L")
    mask_array = np.array(mask)

    print("Dimensões:", mask_array.shape)
    print("Tipo:", mask_array.dtype)
    print("Valores únicos:", np.unique(mask_array))
    print("Pixels defeituosos:", np.count_nonzero(mask_array))

    plt.figure(figsize=(6, 6))
    plt.imshow(mask_array, cmap="gray")
    plt.title(mask_path.name)
    plt.axis("off")

    output_path = PROJECT_ROOT / "experiments" / "output" / "mask_example.png"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(output_path, bbox_inches="tight")
    plt.close()

    print("Imagem salva em:", output_path)


bent_masks = sorted((GROUND_TRUTH_DIR / "bent").glob("*.png"))

if bent_masks:
    inspect_mask(bent_masks[0])

from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="MSherbinii/mvtec-ad-metal-nut",
    repo_type="dataset",
    allow_patterns=["metal_nut/test/**"],
    local_dir="../data/raw/mvtec-ad-metal-nut"
)