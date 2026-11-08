import argparse
import joblib

# 1. Parse CLI arguments
parser = argparse.ArgumentParser(
    description="Predict Iris species from flower measurements"
)

parser.add_argument(
    "--features",
    type=float,
    nargs=4,
    required=True,
    metavar=("SL", "SW", "PL", "PW"),
    help="Sepal length, sepal width, petal length, petal width"
)

args = parser.parse_args()

# 2. Load trained model
model = joblib.load("models/model.joblib")

# 3. Predict
prediction = model.predict([args.features])[0]

# 4. Display result
species = ["setosa", "versicolor", "virginica"]

print(f"Predicted species: {species[prediction]}")