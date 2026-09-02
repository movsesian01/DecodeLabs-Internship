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

## Project 3: Tech Stack Recommender System

### Overview
A Content-Based Recommendation Engine that takes user-input skills and recommends the most matching career path or tech stack using TF-IDF Vectorization and Cosine Similarity.

### Pipeline Architecture
1. **Ingestion**: Accepts user input skills as raw text.
2. **Vector Mapping**: Transforms skill text into TF-IDF vector representations.
3. **Similarity Scoring**: Computes Cosine Similarity between user profile vectors and pre-defined job role skill matrices.
4. **Ranking & Filtering**: Sorts match scores in descending order and displays top recommendations.

### Dataset Structure (`raw_skills.csv`)
Contains job roles (`Data Scientist`, `DevOps Engineer`, `Backend Developer`, `Frontend Developer`, `AI Engineer`) and their associated skill profiles.

### Tech Stack
* **Language**: Python
* **Libraries**: `pandas`, `scikit-learn`, `numpy`

### Performance Metrics
* **Accuracy:** 93.33%
* **Confusion Matrix:**
  ```text
  [[10  0  0]
   [ 0 10  0]
   [ 0  2  8]]
