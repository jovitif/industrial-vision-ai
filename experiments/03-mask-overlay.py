
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_ROOT = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "mvtec-ad-metal-nut"
    / "metal_nut"
)

OUTPUT_DIR = PROJECT_ROOT / "experiments" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def create_overlay(category, filename):
    image_path = (
        DATASET_ROOT / "test" / category / filename
    )

    mask_filename = (
        Path(filename).stem + "_mask.png"
    )

    mask_path = (
        DATASET_ROOT / "ground_truth"
        / category / mask_filename
    )

    image = np.array(
        Image.open(image_path).convert("RGB")
    )

    mask = np.array(
        Image.open(mask_path).convert("L")
    )

    # Verificar compatibilidade das dimensões
    assert image.shape[:2] == mask.shape, (
        "Imagem e máscara possuem dimensões diferentes"
    )

    # Criar uma cópia da imagem
    overlay = image.copy()

    # Destacar os pixels defeituosos em vermelho
    defect_pixels = mask > 0

    red = np.array([255, 0, 0], dtype=np.uint8)

    overlay[defect_pixels] = (
        0.5 * image[defect_pixels] + 0.5 * red
    ).astype(np.uint8)

    # Visualização
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    axes[0].imshow(image)
    axes[0].set_title("Original")

    axes[1].imshow(mask, cmap="gray")
    axes[1].set_title("Ground Truth Mask")

    axes[2].imshow(overlay)
    axes[2].set_title("Mask Overlay")

    for ax in axes:
        ax.axis("off")

    plt.tight_layout()

    output_path = (
        OUTPUT_DIR / f"{category}_{Path(filename).stem}_overlay.png"
    )

    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)

    print(f"Resultado salvo em: {output_path}")


if __name__ == "__main__":
    create_overlay("bent", "000.png")
