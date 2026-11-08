import pandas as pd
from sklearn import datasets
import joblib
from sklearn.ensemble import RandomForestClassifier


# 1. Train the model
iris = datasets.load_iris()
X, y = iris.data, iris.target
model = RandomForestClassifier()
model.fit(X, y)

# 2. Save the model to disk
joblib.dump(model, 'model.joblib')
print("model saved.")