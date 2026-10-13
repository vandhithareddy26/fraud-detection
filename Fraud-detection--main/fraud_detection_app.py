import streamlit as st
import pandas as pd
import joblib 

model = joblib.load("fraud_detection_model.pkl")
st.title("Fraud detection")
st.markdown("Enter details to detect if a given transaction is fraudulant.")
st.divider()

transaction_type = st.selectbox("Transaction Type", ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEPOSIT'])
amount = st.number_input("Amount", min_value= 0.0, value= 1000.0)
oldbalanceOrg = st.number_input("Old balance (sender)", min_value= 0.0, value=1000.0)
newbalanceOrig = st.number_input("New balande (reciever)", min_value=0.0, value= 9000.0)
oldbalanceDest = st.number_input("old  balance(reciever)", min_value=0.0, value= 0.0)
newbalanceDest = st.number_input("New balance (sender)", min_value=0.0, value= 0.0)

if st.button("Predict"):
    input_data = pd.DataFrame([{
            "type": transaction_type,
            "amount": amount,
            "oldbalanceOrg": oldbalanceOrg,
            "newbalanceOrig": newbalanceOrig,
            "oldbalanceDest": oldbalanceDest,
            "newbalanceDest": newbalanceDest
    }])

    predection_model = model.predict(input_data)[0]

    st.subheader(f"prediction: '{int(predection_model)}")
    if predection_model == 1:
        st.error("this transaction can be fraud")
    else:
        st.error("This transaction looks clean.")

