# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Ensure the model folder exists
os.makedirs("model", exist_ok=True)

# Load dataset (CSV file should be in your main folder)
data = pd.read_csv("data/diabetes.csv")

# Prepare data
X = data.drop("Outcome", axis=1)
y = data["Outcome"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "model/diabetes_model.pkl")

print("✅ Model training complete! Saved as 'model/diabetes_model.pkl'")