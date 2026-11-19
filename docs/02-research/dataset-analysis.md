# Dataset Analysis

**Project:** Industrial Vision AI  
**Dataset:** MVTec Anomaly Detection — Metal Nut  
**Category:** `metal_nut`  
**Analysis status:** Structural analysis completed; visual validation pending.

---

## 1. Dataset Overview

The project uses the `metal_nut` category from the MVTec Anomaly Detection (MVTec AD) dataset.

The dataset contains images of metal nuts under normal and defective conditions. It is organized into a training set containing only normal samples, a test set containing normal and anomalous samples, and a ground-truth directory containing segmentation masks for defective samples.

This structure makes the dataset suitable for investigating one-class anomaly detection approaches, where models learn normal appearance patterns and identify deviations during inference.

### Dataset structure

```text
metal_nut/
├── ground_truth/
│   ├── bent/
│   ├── color/
│   ├── flip/
│   └── scratch/
│
├── test/
│   ├── bent/
│   ├── color/
│   ├── flip/
│   ├── good/
│   └── scratch/
│
└── train/
    └── good/
```

---

## 2. Dataset Composition

The dataset contains **335 original images** and **93 ground-truth segmentation masks**, totaling 428 image files.

### 2.1 Training set

The training set contains exclusively normal samples.

| Category | Number of images |
|---|---:|
| Good | 220 |
| **Total** | **220** |

This composition supports experiments with anomaly detection methods trained on normal data without requiring defective samples during training.

### 2.2 Test set

The test set contains normal samples and four defect categories.

| Category | Number of images |
|---|---:|
| Good | 22 |
| Bent | 25 |
| Color | 22 |
| Flip | 23 |
| Scratch | 23 |
| **Total** | **115** |

The test set contains:

- 22 normal images.
- 93 defective images.
- 4 distinct defect categories.

### 2.3 Ground-truth masks

| Defect category | Number of masks |
|---|---:|
| Bent | 25 |
| Color | 22 |
| Flip | 23 |
| Scratch | 23 |
| **Total** | **93** |

Each defective test image has a corresponding ground-truth mask.

---

## 3. Image Properties

### 3.1 Resolution

All 335 original images were inspected.

Every image has the same resolution:

| Property | Result |
|---|---|
| Width | 700 pixels |
| Height | 700 pixels |
| Resolution | 700 × 700 |
| Aspect ratio | 1:1 |
| Pixels per image | 490,000 |
| Resolution variations | None detected |

The uniform resolution simplifies preprocessing and provides consistent input dimensions for model experiments.

### 3.2 File formats

The image files were inspected using their actual image formats rather than relying exclusively on file extensions.

| Property | Result |
|---|---|
| File extension | `.png` |
| Actual image format | PNG |
| Total image files | 428 |
| Other formats detected | None |

PNG is a lossless image format, which avoids introducing additional compression artifacts into the original dataset.

### 3.3 Image modes

The image modes were also inspected.

| Image type | Mode | Number of files |
|---|---|---:|
| Original images | RGB | 335 |
| Ground-truth masks | L (grayscale) | 93 |
| **Total** | | **428** |

Original images contain three color channels, while segmentation masks use a single grayscale channel.

---

## 4. Ground-Truth Mask Analysis

Ground-truth masks provide pixel-level annotations identifying defective regions.

### 4.1 Mask dimensions

All masks were checked against their corresponding test images.

No dimensional mismatches were reported.

| Property | Result |
|---|---|
| Mask resolution | 700 × 700 |
| Image-mask dimension mismatches | 0 |
| Missing masks | 0 |
| Missing corresponding images | 0 |

### 4.2 Pixel encoding

A sample of 12 masks was inspected across the four defect categories.

All inspected masks presented the following pixel values:

| Pixel value | Interpretation |
|---|---|
| 0 | Background / non-defective region |
| 255 | Annotated defective region |

The inspected masks were binary grayscale images.

**Validation scope:** 12 of the 93 masks were inspected for pixel-value encoding. The binary encoding of the remaining masks has not yet been independently verified.

### 4.3 Image-mask correspondence

The correspondence between defective test images and ground-truth masks was checked using their filenames.

The expected naming convention is:

```text
test/<category>/<filename>.png
ground_truth/<category>/<filename>_mask.png
```

The structural validation produced the following results:

| Category | Test images | Masks | Missing masks | Missing images |
|---|---:|---:|---:|---:|
| Bent | 25 | 25 | 0 | 0 |
| Color | 22 | 22 | 0 | 0 |
| Flip | 23 | 23 | 0 | 0 |
| Scratch | 23 | 23 | 0 | 0 |
| **Total** | **93** | **93** | **0** | **0** |

All 93 defective test images have a corresponding mask with matching dimensions.

This confirms structural correspondence based on filenames and dimensions. Visual alignment between the annotated regions and the actual defects still requires visual inspection.

---

## 5. Defect Categories

The dataset contains four types of anomalies.

| Category | Description |
|---|---|
| Bent | Deformation of the metal nut |
| Color | Abnormal color or surface appearance |
| Flip | Abnormal orientation or positioning |
| Scratch | Surface scratches |

These categories provide different anomaly characteristics and allow evaluation across multiple defect types.

The project will investigate whether anomaly detection models can identify these defects and localize their corresponding regions.

---

## 6. Dataset Suitability for Anomaly Detection

The dataset has several characteristics that make it suitable for an anomaly detection experiment.

### 6.1 Normal-only training data

The training set contains only 220 normal images.

This enables experimentation with methods that learn the distribution of normal samples and detect deviations during inference.

Potential approaches include:

- PatchCore
- PaDiM
- EfficientAD
- Feature embedding-based anomaly detection

### 6.2 Pixel-level annotations

The 93 ground-truth masks provide spatial annotations for defective regions.

These annotations make it possible to evaluate not only whether an image contains an anomaly, but also whether the model correctly identifies the location of the defect.

### 6.3 Multiple defect categories

The four defect categories allow the evaluation of model behavior across different anomaly patterns.

However, the relatively small number of test samples per category should be considered when interpreting evaluation results.

---

## 7. Dataset Limitations

The following limitations are based on the dataset structure and the measurements performed during this analysis.

### 7.1 Limited number of samples

The dataset contains:

- 220 normal training images.
- 22 normal test images.
- 93 defective test images.

The limited number of samples may restrict the statistical reliability of evaluation results, particularly when analyzing individual defect categories.

### 7.2 Single product category

The analysis focuses exclusively on metal nuts.

Therefore, model performance on this dataset does not demonstrate generalization to other industrial components, materials, or product geometries.

### 7.3 Limited defect diversity

Only four defect categories are available:

- Bent
- Color
- Flip
- Scratch

Other possible industrial defects are not represented in this category.

### 7.4 Normal-only training distribution

The training set contains only normal samples.

Although this is appropriate for one-class anomaly detection, it does not provide defective training examples for supervised classification of individual defect types.

### 7.5 Fixed image resolution

All original images have a resolution of 700 × 700 pixels.

This consistency simplifies preprocessing, but the dataset does not establish how a model would perform with images acquired at different resolutions.

### 7.6 Production environment constraints

The dataset analysis does not establish performance under real production-line conditions, such as varying illumination, camera configurations, component positioning, mechanical vibration, or processing-speed requirements.

These factors should be considered when discussing the limitations of transferring an experimental model into an industrial environment.

---

## 8. Data Quality and Validation Summary

The following table summarizes the checks performed.

| Validation | Result | Status |
|---|---|---|
| Dataset directory structure | Verified | Complete |
| Training image count | 220 | Complete |
| Test image count | 115 | Complete |
| Ground-truth mask count | 93 | Complete |
| Image resolution | 700 × 700 | Complete |
| Image format | PNG | Complete |
| Image modes | RGB / L | Complete |
| Sample mask encoding | Binary (0 and 255) in 12 masks | Partial |
| Image-mask filename correspondence | 93/93 | Complete |
| Image-mask dimension correspondence | 93/93 | Complete |
| Visual image-mask alignment | Not yet inspected | Pending |
| All-mask pixel encoding validation | Not yet performed | Pending |

---

## 9. Conclusion

The `metal_nut` dataset provides a structured environment for investigating industrial anomaly detection and defect localization.

The analysis confirmed 220 normal training images, 115 test images, and 93 corresponding ground-truth masks across four defect categories.

All original images have a consistent resolution of 700 × 700 pixels and are stored in PNG format. Structural correspondence between all defective test images and their masks was also verified.

The normal-only training distribution makes the dataset appropriate for experimenting with one-class anomaly detection methods, while the ground-truth masks provide the necessary annotations for evaluating defect localization.

Some validation activities remain pending, particularly the inspection of all mask pixel values and visual confirmation of image-mask alignment.

The next project phase will focus on preparing the data pipeline, defining preprocessing procedures, implementing baseline models, and establishing reproducible evaluation experiments.