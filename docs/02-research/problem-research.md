# Problem Research — Industrial Vision AI

## 1. Problem Overview

Industrial quality inspection is an essential process in manufacturing environments, particularly in industries where product defects can compromise safety, reliability, performance, and production costs.

Traditional manual inspection depends heavily on human operators, making the process susceptible to fatigue, inconsistencies, subjective judgment, and operational limitations.

Industrial Vision AI explores the application of Computer Vision and Machine Learning techniques to support automated visual quality inspection.

The project focuses on identifying defective metal nuts through image analysis.

## 2. Industrial Context

**Industry:** Automotive / Manufacturing  
**Inspection Target:** Metal nuts  
**Technology Domain:** Computer Vision and Machine Learning  
**Problem Type:** Visual Anomaly Detection and Defect Localization

Metal nuts are mechanical components used in fastening applications. Their dimensional integrity, surface condition, and correct positioning are important for ensuring product quality.

Visual inspection can help identify abnormalities that may otherwise pass unnoticed during manufacturing.

## 3. Problem Statement

The objective is to investigate how a computer vision system can distinguish normal metal nuts from defective samples and identify the regions associated with visual anomalies.

The system should explore two complementary capabilities:

1. **Anomaly Detection:** Determine whether an inspected component presents an abnormality.
2. **Anomaly Localization:** Identify the image regions associated with the detected defect.

The initial investigation will use the Metal Nut dataset, which contains normal and defective samples organized into different categories.

## 4. Defect Categories

The dataset provides four defect categories:

| Category | Description |
|---|---|
| Bent | Deformation or bending of the metal nut |
| Color | Abnormal color or surface appearance |
| Flip | Incorrect orientation or positioning |
| Scratch | Scratches or surface damage |

Normal samples are also available and will serve as the reference for learning the expected visual appearance of the component.

## 5. Research Questions

The project will investigate the following questions:

- Can a model learn the visual characteristics of normal metal nuts?
- Can the model distinguish normal samples from defective ones?
- Can different defect types be detected reliably?
- Can the defective regions be localized through segmentation?
- How do image resolution, lighting, positioning, and surface variations affect model performance?
- Which evaluation metrics are appropriate for industrial anomaly detection?

## 6. Proposed Technical Approach

The project will initially investigate an anomaly detection approach based on normal training samples.

The proposed workflow consists of:

1. Dataset exploration and validation.
2. Image preprocessing and normalization.
3. Feature extraction and visual representation.
4. Anomaly detection model development.
5. Defect localization and segmentation.
6. Model evaluation and error analysis.

Potential approaches to investigate include:

- Convolutional Neural Networks (CNNs).
- Transfer Learning.
- Feature Embeddings.
- Patch-based Anomaly Detection.
- Industrial Anomaly Detection architectures.

Potential model candidates include PatchCore, PaDiM, and EfficientAD.

The final architecture will be selected after dataset exploration and baseline experimentation.

## 7. Evaluation Strategy

The system will be evaluated at two levels:

**Image-level evaluation**

Determines whether an entire sample is normal or anomalous.

Potential metrics:
- AUROC.
- Precision.
- Recall.
- F1-score.

**Pixel-level evaluation**

Measures the model's ability to identify defective regions.

Potential metrics:
- Pixel-level AUROC.
- AUPRO.
- Intersection over Union (IoU).
- Dice Score.

The availability and suitability of ground-truth segmentation masks will be considered during evaluation.

## 8. Project Scope

### Included

- Industrial image inspection.
- Normal and defective sample analysis.
- Anomaly detection.
- Defect localization.
- Segmentation-based evaluation.
- Model experimentation.
- Reproducible experiments and documentation.

### Not Included in the Initial Scope

- Real-time industrial production deployment.
- Physical integration with manufacturing equipment.
- Robotic inspection systems.
- Production-grade edge deployment.
- Certification for industrial safety applications.

## 9. Expected Outcome

The expected outcome is a reproducible Computer Vision project demonstrating the development and evaluation of an industrial visual inspection system.

The project should provide:

- A documented dataset analysis.
- A reproducible preprocessing pipeline.
- At least one baseline anomaly detection model.
- Quantitative evaluation results.
- Visual examples of anomaly localization.
- Technical documentation describing design decisions and limitations.

## 10. Research Principle

The project will prioritize experimental rigor, reproducibility, and transparent reporting.

Model performance must be supported by quantitative evaluation rather than visual examples alone.

All limitations, assumptions, and experimental decisions should be documented.