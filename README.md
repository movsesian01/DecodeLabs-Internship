# DecodeLabs-Internship
This repository contains projects, tasks, and code developed during the **DecodeLabs Virtual Internship**.

## 🤖 Projects


---

## Project 1: Rule-Based Conversational Chatbot

### Overview
An interactive Python chatbot built to handle user inquiries, extract key entities, and guide users through structured conversation flows using rule-based decision trees.

### Key Features
* **Pattern Matching**: Evaluates user intent through customized string and keyword analysis.
* **Fallback Mechanisms**: Handles unrecognized inputs with contextual default responses.
* **CLI Interface**: Real-time terminal output for seamless user interaction.

### Tech Stack
* **Language**: Python

---

## Project 2: K-Nearest Neighbors (KNN) Customer Classification Pipeline

### Overview
A supervised machine learning classification pipeline designed to analyze customer behavioral data and classify target segments using the K-Nearest Neighbors (KNN) algorithm.

### Pipeline Steps
1. **Data Ingestion & Preprocessing**: Loads dataset, cleans missing values, and encodes categorical variables.
2. **Feature Scaling**: Standardizes numeric attributes using `StandardScaler` to balance distance metrics.
3. **Model Training**: Configures and trains a `KNeighborsClassifier` model.
4. **Evaluation**: Evaluates performance using classification metrics including Accuracy, Precision, Recall, and Confusion Matrices.

### Tech Stack
* **Language**: Python
* **Libraries**: `pandas`, `scikit-learn`, `numpy`

---

## Project 3: Tech Stack & Career Path Recommender System

### Overview
A Content-Based Recommendation Engine that processes user-submitted skill sets and identifies the most aligned career roles or tech stacks using natural language processing (NLP) vectorization techniques.

### Recommender Architecture
1. **Ingestion**: Captures user input skills from the terminal interface.
2. **Vector Mapping**: Converts text data into numerical feature matrices using **TF-IDF (Term Frequency-Inverse Document Frequency) Vectorization**.
3. **Similarity Scoring**: Measures vector proximity between user input and job profiles using **Cosine Similarity**.
4. **Sorting & Filtering**: Ranks similarity scores in descending order to output top-N recommendations with match percentages.

### Dataset (`raw_skills.csv`)
Stores predefined target job roles (`Data Scientist`, `DevOps Engineer`, `Backend Developer`, `Frontend Developer`, `AI Engineer`) alongside their core technology skill profiles.

### Tech Stack
* **Language**: Python
* **Libraries**: `pandas`, `scikit-learn`, `numpy`

---

## How to Run locally

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/movsesian01/DecodeLabs-Internship.git](https://github.com/movsesian01/DecodeLabs-Internship.git)
   cd DecodeLabs-Internship
