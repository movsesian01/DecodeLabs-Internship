import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

iris=load_iris()
X=iris.data
y=iris.target
target_names = iris.target_names

print("--- DATASET INFORMATION ---")
print(f"Total samples loaded: {X.shape[0]}")
print(f"Features measured: {X.shape[1]}")
print(f"Target flower types: {list(target_names)}\n")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

model=KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)

predictions=model.predict(X_test_scaled)

print("--- MODEL EVALUATION RESULTS ---")
print(f"Overall Accuracy: {accuracy_score(y_test, predictions) * 100:.2f}%\n")

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nDetailed Performance Metrics (Precision, Recall, F1-Score):")
print(classification_report(y_test, predictions, target_names=target_names))