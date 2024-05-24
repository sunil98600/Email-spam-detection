# Spam Mail Classification Project

This project demonstrates a basic spam mail classification system using machine learning techniques. The system is built using Python and various libraries including pandas, scikit-learn, and NumPy.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Example Predictions](#example-predictions)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The goal of this project is to classify email messages as spam or not spam using a Naive Bayes classifier. The dataset used is a collection of SMS messages labeled as 'spam' or 'ham' (non-spam).

## Installation

To get started, clone the repository and install the required packages:

```bash
git clone https://github.com/your-username/spam-mail-classification.git
cd spam-mail-classification
pip install -r requirements.txt
```

## Usage

To run the spam classification script, follow these steps:

1. **Load the dataset:** Ensure the dataset (`spam.csv`) is in the same directory as your script.
2. **Run the script:** Execute the script to train the model and make predictions.

```bash
python spam_classification.py
```

## Project Structure

```
spam-mail-classification/
├── spam_classification.py
├── spam.csv
├── requirements.txt
├── README.md
```

- `spam_classification.py`: The main script that performs data loading, preprocessing, model training, and prediction.
- `spam.csv`: The dataset containing labeled SMS messages.
- `requirements.txt`: A list of required Python packages.
- `README.md`: This file.

## Model Training and Evaluation

The script performs the following steps:

1. **Data Loading:** Reads the dataset using pandas.
2. **Data Preprocessing:** Cleans and prepares the data for model training.
3. **Feature Extraction:** Uses `CountVectorizer` to convert text data into numerical features.
4. **Model Training:** Trains a Naive Bayes classifier using the training data.
5. **Model Evaluation:** Evaluates the model's accuracy on the test data.
6. **Prediction:** Predicts whether new messages are spam or not.

### Example Predictions

Here is an example of how to use the trained model to make predictions:

```python
emails = [
    'Sounds great! Are you home now?',
    'Will u meet ur dream partner soon? Is ur career off 2 a flyng start? 2 find out free, txt HORO followed by ur star sign, e.g., HORO ARIES'
]

predictions = clf.predict(emails)
print(predictions)  # Output: [0 1]
```

And here is an example of evaluating the model:

```python
accuracy = clf.score(X_test, y_test)
print(f"Model Accuracy: {accuracy}")
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

Feel free to reach out if you have any questions or need further assistance.
