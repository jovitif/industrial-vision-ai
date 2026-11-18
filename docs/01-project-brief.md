# Industrial Vision AI

**Project Brief — v0.2**

| Property | Definition |
|---|---|
| Project | Industrial Vision AI |
| Type | Experimental Software Engineering Project |
| Domain | Industrial Quality Inspection |
| Context | Automotive Industry |
| Technology Area | Computer Vision and Machine Learning |
| Status | Discovery / Planning |
| Owner | Independent Development |

## 1. Executive Summary

Industrial Vision AI is an experimental project that proposes the development of a software solution to support visual quality inspection processes in industrial environments, with a focus on the automotive industry.

The solution will use computer vision and machine learning techniques to analyze images of metal components, identify potential visual anomalies, and record inspection results.

The initial experimental component will be a metal nut, using images from a public dataset to develop and evaluate anomaly detection methods.

The project aims to investigate the technical feasibility of using artificial intelligence as a tool to support visual inspection, without assuming that automation will replace human evaluation.

## 2. Problem Statement

Visual inspection of industrial components is an important activity for identifying potential non-conformities during manufacturing processes.

However, anomaly detection can present challenges related to variations in the visual characteristics of components, image acquisition conditions, and the occurrence of small or barely noticeable defects.

The limited availability of defective samples also presents a challenge for developing traditional supervised classification models.

In this context, there is an opportunity to investigate anomaly detection techniques capable of learning the visual characteristics of components considered normal and identifying potential deviations in new images.

**Core Problem:**

How can a software solution be developed to identify potential visual anomalies in metal components through image analysis, using computer vision and machine learning techniques?

## 3. Objectives

### 3.1. General Objective

Develop an intelligent visual inspection prototype capable of detecting and localizing potential anomalies in metal components using computer vision and machine learning techniques.

### 3.2. Specific Objectives

- Investigate anomaly detection techniques applied to industrial inspection.
- Identify and prepare a dataset suitable for the experiment.
- Develop a model capable of learning the visual characteristics of normal components.
- Detect potential anomalies in images not used during training.
- Generate anomaly maps to highlight visually suspicious regions.
- Provide an API for integration with the application's components.
- Store images, results, and inspection information.
- Develop an interface for querying and validating inspection results.
- Evaluate model performance using appropriate metrics.
- Investigate the influence of variations in image acquisition conditions on the results.

## 4. Project Scope

### 4.1. In Scope

- Experimental inspection of metal nuts.
- Image reception and processing.
- Anomaly detection using machine learning.
- Visual localization of suspicious regions.
- Classification of inspection outcomes as normal, suspected anomaly, or processing failure.
- Storage of inspection results.
- Access to inspection history.
- Human validation of results.
- Visualization of basic quality indicators.
- Experimental model evaluation.

### 4.2. Out of Scope (Initial Phase)

- Integration with physical industrial cameras and sensors.
- Integration with actual production conveyor belts.
- Automatic control of industrial machinery.
- Physical rejection of components on the production line.
- Identification of all types of automotive defects.
- Inspection of complete vehicles.
- Guaranteed operation in real industrial environments.
- Training large-scale models from scratch.

## 5. Stakeholders

Since this is an independent project, stakeholders are defined hypothetically based on the intended application context.

| Stakeholder | Interest |
|---|---|
| Quality Inspector | Review inspection results and validate potential defects |
| Quality Analyst | Monitor quality indicators and occurrences |
| Production Engineer | Identify potential issues in the manufacturing process |
| Industrial Manager | Monitor inspection results and reliability |
| Technology Team | Develop, integrate, and maintain the solution |

**Primary User:** Quality Inspector, responsible for evaluating images and validating the results presented by the system.

## 6. Assumptions and Constraints

### 6.1. Assumptions

- The experiment will use publicly available images of industrial components.
- Images will be considered representative only of the experimental scenario defined by the selected dataset.
- The model will initially be trained using images of defect-free components.
- The application will be developed without depending on actual industrial equipment.
- AI-generated results will be treated as indications of potential anomalies, not as definitive quality decisions.

### 6.2. Constraints

- Individual development with limited computational resources.
- No access to an actual production line.
- No access to industrial optical sensors.
- Dependence on the characteristics and limitations of the selected dataset.
- Evaluation limited to the selected component category.
- Inability to claim industrial reliability without validation in a real production environment.
- Licensing restrictions associated with the data used.

## 7. Dataset and Experimental Component

**Selected Dataset:** MVTec Anomaly Detection (MVTec AD).

**Selected Category:** Metal Nut.

The dataset provides images of different industrial objects and surfaces, including metal nuts, with both normal and anomalous samples.

Its data structure supports anomaly detection experiments using normal images for training and both normal and defective images for evaluation.

The dataset also provides ground-truth masks for localizing anomalous regions.

### Rationale for Selection

- Compatibility with the visual inspection problem.
- Availability of real industrial images.
- Presence of both normal and anomalous samples.
- Availability of annotations for evaluation.
- Opportunity to experiment with anomaly detection techniques without building a custom dataset.

## 8. Expected Outcomes

By the end of the project, the expected deliverables are:

- An experimental anomaly detection model.
- An inference service accessible through an API.
- An application for managing and querying inspections.
- A mechanism for visualizing suspicious regions.
- A historical record of inspection results.
- An evaluation report containing metrics, experiments, and limitations.
- Technical documentation describing the solution and its architecture.

## 9. Success Criteria

The project will be considered technically demonstrated when:

1. The system can receive and process images.
2. The model can generate an anomaly score.
3. The model can distinguish normal and anomalous samples with measurable performance.
4. The system can generate a visual representation of suspicious regions.
5. Results can be stored and retrieved.
6. Performance can be evaluated using reproducible metrics.
7. The experiment's limitations are documented.

No artificial accuracy target will be established before the experiments are conducted. Results must be measured and analyzed against a baseline.

## 10. Known Limitations

The prototype will be developed using a public dataset, which does not necessarily represent the conditions found on an automotive production line.

The performance achieved in the experiment cannot be directly interpreted as a guarantee of industrial performance.

Generalization to other components, materials, cameras, and lighting conditions will require additional experiments.

## 11. Current Status

Project currently in the discovery and planning phase.

The next activities involve technical research, dataset analysis, requirements definition, and the development of an initial proof of concept.