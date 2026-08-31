# DecodeLabs-Internship
This repository contains projects, tasks, and code developed during the **DecodeLabs Virtual Internship**.

## 🤖 Projects

## Project 1: Rule-Based AI Chatbot
* **File:** `chatbot.py`
* **Description:** A rule-based conversational chatbot designed to process natural language inputs and deliver contextual responses using predefined logic.

---

## Project 2: Supervised Learning - KNN Iris Classification
* **File:** `classification.py`
* **Description:** A supervised machine learning pipeline using the K-Nearest Neighbors (KNN) algorithm to classify flower species from the standard Iris benchmark dataset.

### Pipeline Highlights
* **Dataset Ingestion:** Loaded the Iris dataset (150 samples across 3 flower classes: *Setosa*, *Versicolor*, *Virginica*).
* **Preprocessing:** Split data into an 80/20 train-test ratio (`stratify=y`) and scaled numerical features using `StandardScaler`.
* **Model Training:** Built and trained a `KNeighborsClassifier` ($K=5$).
* **Evaluation:** Achieved **93.33% Overall Accuracy** on unseen test data.

### Performance Metrics
* **Accuracy:** 93.33%
* **Confusion Matrix:**
  ```text
  [[10  0  0]
   [ 0 10  0]
   [ 0  2  8]]
