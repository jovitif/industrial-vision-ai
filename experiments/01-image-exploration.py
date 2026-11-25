from datasets import load_dataset

ds = load_dataset("MSherbinii/mvtec-ad-metal-nut")

from pathlib import Path

OUTPUT_DIR = Path("experiments/output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print(ds)

print("Divisões disponíveis:", ds.keys())

for split in ds:
    print(f"\nSplit: {split}")
    print(ds[split])
    print("Colunas:", ds[split].column_names)

import matplotlib.pyplot as plt

sample = ds["train"][0]

image = sample["image"]

plt.imshow(image)
plt.title("Metal Nut")
plt.axis("off")
plt.show()

import numpy as np

image_array = np.array(image)

print("Dimensões:", image_array.shape)
print("Tipo:", image_array.dtype)
print("Valor mínimo:", image_array.min())
print("Valor máximo:", image_array.max())

import cv2

image_bgr = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)

gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

resized = cv2.resize(image_bgr, (256, 256))

blurred = cv2.GaussianBlur(image_bgr, (5, 5), 0)

fig, axes = plt.subplots(1, 4, figsize=(16, 4))

axes[0].imshow(image_array)
axes[0].set_title("Original")

axes[1].imshow(gray, cmap="gray")
axes[1].set_title("Grayscale")

axes[2].imshow(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB))
axes[2].set_title("Resized")

axes[3].imshow(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))
axes[3].set_title("Blurred")

for ax in axes:
    ax.axis("off")

plt.tight_layout()
plt.show()

from collections import Counter

# Verificar os recursos e tipos de dados
print("Features do dataset:")
print(ds["train"].features)

# Analisar distribuição dos rótulos
for split in ds:
    labels = ds[split]["label"]

    print(f"\n--- {split.upper()} ---")
    print("Total de imagens:", len(labels))
    print("Distribuição dos labels:", Counter(labels))
    print("Labels encontrados:", sorted(set(labels)))

import matplotlib.pyplot as plt

def compare_images(dataset, indices, split):
    fig, axes = plt.subplots(
        1, len(indices),
        figsize=(4 * len(indices), 4)
    )

    if len(indices) == 1:
        axes = [axes]

    for ax, index in zip(axes, indices):
        sample = dataset[split][index]

        ax.imshow(sample["image"])
        ax.set_title(
            f"Index: {index}\nLabel: {sample['label']}"
        )
        ax.axis("off")

    plt.tight_layout()

    output_path = OUTPUT_DIR / f"{split}_comparison.png"

    plt.savefig(
        output_path,
        dpi=150,
        bbox_inches="tight"
    )

    plt.close(fig)

    print(f"Imagem salva em: {output_path}")

compare_images(ds, [0, 1, 2, 3, 4], "train")
compare_images(ds, [0, 1, 2, 3, 4], "test")

print("Colunas:", ds["test"].column_names)
print("Features:", ds["test"].features)
print("Exemplo:", ds["test"][0])

from collections import Counter

print("Quantidade de imagens:", len(ds["train"]))

print("\nPrimeiras amostras:")

for i in range(10):
    sample = ds["train"][i]

    print(
        f"Index: {i} | "
        f"Label: {sample['label']} | "
        f"Image size: {sample['image'].size}"
    )

features = ds["test"].features["label"]

for label, count in sorted(
    Counter(ds["test"]["label"]).items()
):
    class_name = features.int2str(label)

    print(f"{class_name}: {count} imagens")

import matplotlib.pyplot as plt

label_feature = ds["test"].features["label"]

def compare_classes(dataset):
    labels = dataset["test"]["label"]
    num_classes = label_feature.num_classes

    fig, axes = plt.subplots(
        1, num_classes,
        figsize=(4 * num_classes, 5)
    )

    for label_id in range(num_classes):
        # Encontrar a primeira imagem de cada classe
        index = next(
            i for i, label in enumerate(labels)
            if label == label_id
        )

        sample = dataset["test"][index]
        class_name = label_feature.int2str(label_id)

        axes[label_id].imshow(sample["image"])
        axes[label_id].set_title(class_name)
        axes[label_id].axis("off")

    plt.tight_layout()

    output_path = OUTPUT_DIR / "test_class_comparison.png"

    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)

    print(f"Comparação salva em: {output_path}")


compare_classes(ds)

from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="MSherbinii/mvtec-ad-metal-nut",
    repo_type="dataset",
    allow_patterns="metal_nut/ground_truth/**",
    local_dir="../data/raw/mvtec-ad-metal-nut"
)