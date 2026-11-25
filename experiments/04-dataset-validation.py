
from pathlib import Path
import numpy as np
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_ROOT = (
    PROJECT_ROOT
    / "data/raw/mvtec-ad-metal-nut/metal_nut"
)

CATEGORIES = ["bent", "color", "flip", "scratch"]

total_images = 0
total_masks = 0
errors = []

for category in CATEGORIES:
    image_dir = DATASET_ROOT / "test" / category
    mask_dir = DATASET_ROOT / "ground_truth" / category

    images = sorted(image_dir.glob("*.png"))
    masks = sorted(mask_dir.glob("*_mask.png"))

    print(f"\nCategoria: {category}")
    print(f"Imagens: {len(images)}")
    print(f"Máscaras: {len(masks)}")

    total_images += len(images)
    total_masks += len(masks)

    for image_path in images:
        mask_path = mask_dir / f"{image_path.stem}_mask.png"

        if not mask_path.exists():
            errors.append(f"Máscara ausente: {mask_path}")
            continue

        image = Image.open(image_path)
        mask = Image.open(mask_path)

        if image.size != mask.size:
            errors.append(f"Dimensões incompatíveis: {image_path.name}")

        mask_array = np.array(mask.convert("L"))
        values = set(np.unique(mask_array))

        if not values.issubset({0, 255}):
            errors.append(f"Valores inesperados: {mask_path.name}")

print("\n--- RESULTADO FINAL ---")
print("Total de imagens:", total_images)
print("Total de máscaras:", total_masks)
print("Problemas encontrados:", len(errors))

for error in errors:
    print(error)

if not errors:
    print("Validação concluída sem inconsistências!")
