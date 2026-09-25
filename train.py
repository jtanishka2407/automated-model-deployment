import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset from CSV
data = pd.read_csv("data/data.csv")

X = data[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
y = data["target"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = RandomForestClassifier(random_state=42)

# Train model
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)

# Save model
joblib.dump(model, "model.pkl")

print("Model saved successfully!")