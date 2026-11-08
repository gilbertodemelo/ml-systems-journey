# Project 01 — Machine Learning CLI

A simple command-line application that trains a machine learning model and uses it to make predictions.

This is the first project in my **ML Systems Journey**, a series of hands-on projects focused on building practical skills in ML Systems.

## Objective

Learn how to move a machine learning model from a development environment into a standalone Python application.

The project demonstrates how to:

- Train a classification model using scikit-learn.
- Serialize and save a trained model.
- Load the model in a separate Python process.
- Accept input parameters through a command-line interface (CLI).
- Generate predictions without using a Jupyter notebook.

## Tech Stack

- Python 3
- scikit-learn
- joblib
- argparse (Python standard library)

## Project Structure

```text
01-ml-cli/
├── train.py
├── predict.py
├── requirements.txt
├── models/
│   └── model.joblib
└── README.md
```

## Dataset

The project uses the Iris dataset, a classic classification dataset containing 150 flower samples belonging to three species:

- Setosa
- Versicolor
- Virginica

Each sample contains four numerical features:

1. Sepal length (cm)
2. Sepal width (cm)
3. Petal length (cm)
4. Petal width (cm)

## Model

The classifier is implemented using scikit-learn's `LogisticRegression`.

The trained model is serialized using `joblib` and saved to the `models/` directory.

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/<your-username>/ml-systems-journey.git
cd ml-systems-journey/01-ml-cli
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Train the model

```bash
python train.py
```

This command trains the classifier and saves the trained model to:

```text
models/model.joblib
```

### 2. Run a prediction

```bash
python predict.py --features 5.1 3.5 1.4 0.2
```

Example output:

```text
Predicted species: