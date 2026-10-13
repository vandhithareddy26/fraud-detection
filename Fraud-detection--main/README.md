# Fraud Detection App

A simple Streamlit web app that predicts whether a financial transaction is likely to be fraudulent based on transaction details and account balance information.

## Overview

This project uses a trained machine learning model to analyze a transaction and classify it as:

- `1` = Fraudulent
- `0` = Legitimate / Clean

The app accepts basic transaction information such as transaction type, amount, and sender/receiver balance values, then returns a prediction instantly in the browser.

## Features

- User-friendly interface built with Streamlit
- Transaction type selection
- Amount and balance inputs
- Real-time fraud prediction
- Clear result display with fraud risk messaging

## Tech Stack

- Python
- Streamlit
- pandas
- scikit-learn / trained model artifact
- joblib

## Project Files

- `fraud_detection_app.py` - Streamlit app
- `fraud_detection_model.pkl` - Trained machine learning model
- `AIML Dataset.csv` - Dataset used for model training
- `fraud detection.ipynb` - Notebook for model exploration and training

## Prerequisites

Make sure you have Python 3.9+ installed on your machine.

## Installation

1. Clone or download the project folder.
2. Open a terminal in the project directory.
3. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

4. Install the required packages:

```bash
pip install streamlit pandas scikit-learn joblib
```

## Run the App

From the project directory, run:

```bash
streamlit run fraud_detection_app.py
```

This will open the app in your default web browser.

## How to Use

1. Select the transaction type.
2. Enter the amount and balance values.
3. Click the Predict button.
4. View the prediction result and fraudulent risk status.

## Important Note

The app is a lightweight demo that predicts fraud using a pre-trained model file. For better accuracy or to retrain the model, you can use the notebook in the project and regenerate the `.pkl` model file.

## Example Inputs

Typical inputs include:

- Transaction type: PAYMENT, TRANSFER, CASH_OUT, DEPOSIT
- Amount: e.g. 5000
- Sender old balance: e.g. 12000
- Sender new balance: e.g. 7000
- Receiver old balance: e.g. 0
- Receiver new balance: e.g. 9000

## License

This project is intended for educational and demonstration purposes.
