from datasets import load_dataset

ds = load_dataset("MSherbinii/mvtec-ad-metal-nut")

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