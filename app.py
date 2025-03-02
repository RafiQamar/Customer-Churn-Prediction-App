# import necessary libraries
import streamlit as st
import pickle
import pandas as pd

# Load the categorical variable encoder
with open('encoders.pkl', 'rb') as f:
    encoder = pickle.load(f)
# Load the target encoder
with open('target_encoder.pkl', 'rb') as f:
    target_encoder = pickle.load(f)
# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
# Load the standardizing scaler
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Creating an Input Interface 
st.title('Customer Churn Prediction')

gender = st.selectbox('Gender:', ['Male', 'Female'])
senior_citizen = st.selectbox('Is senior citizen?', [0, 1])
partner = st.selectbox('Has a partner?', ['Yes', "No"])
dependent = st.selectbox('Has dependents?', ['Yes', 'No'])
tenure = st.number_input('Number of months customer has stayed:', min_value=1.0, max_value=72.0, step=1.0)
phone_service = st.selectbox('Has phone service?', ['Yes', "No"])
multi_line = st.selectbox('Has multiple lines?', ['Yes', "No"])
internet_service = st.selectbox('Internet service provider?',['DSL', 'Fiber optic', 'No'])
online_security = st.selectbox('Has online security service?', ['Yes', "No"])
online_backup  = st.selectbox('Has online backup service?', ['Yes', "No"])
device_protection = st.selectbox('Has device protection service?', ['Yes', "No"])
tech_support  = st.selectbox('Has tech support service?', ['Yes', "No"])
streaming_tv = st.selectbox('Has streaming TV service?', ['Yes', "No"])
streaming_movies  = st.selectbox('Has streaming movies service?', ['Yes', "No"])
contract_type = st.selectbox('Which contract type customer has?', ['Month-to-month', 'One year', 'Two year'])
paper_billing = st.selectbox('Customer get paper bill?', ['Yes', "No"])
payment = st.selectbox('Choose payment method:', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
monthly_charge = st.number_input('How much customer paid monthly', min_value=18.0, max_value=120.0, step=0.1)
total_charge = st.number_input('How much customer paid in total', min_value=18.0, max_value=9000.0, step=0.1)

l = [ 'Partner', 'Dependents', 'MultipleLines', 'InternetService',
       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
       'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
       'PaymentMethod']

num_col = ['tenure', 'MonthlyCharges']

# Preparing the input to feed the model

raw_input = pd.DataFrame({'SeniorCitizen' : [senior_citizen],
              'Partner': [partner], 
              'Dependents': [dependent], 
              'tenure': [tenure], 
              'MultipleLines': [multi_line],
              'InternetService': [internet_service], 
              'OnlineSecurity': [online_security], 
              'OnlineBackup': [online_backup],  
              'DeviceProtection': [device_protection],
              'TechSupport': [tech_support], 
              'StreamingTV': [streaming_tv], 
              'StreamingMovies': [streaming_movies], 
              'Contract': [contract_type],
              'PaperlessBilling': [paper_billing],
              'PaymentMethod': [payment],
              'MonthlyCharges': [monthly_charge]
             })

for col in l:
    raw_input[col] = encoder[col].transform(raw_input[col])

raw_input[num_col] = scaler.transform(raw_input[num_col])


if st.button('Predict: Will this customer churn?'):
    pred = model.predict(raw_input)
    # Predict and inverse transform the prediction to the original scale
    prediction = target_encoder.inverse_transform(pred.reshape(-1, 1))
    result = prediction[0]
    # Display Predictions
    st.write(f"{result}")

    # Advice based on churn prediction
    if result == 'Yes':  
        # Provide retention strategies
        st.title("Advice to Retain Customer:")
        if monthly_charge > 80:
            st.write("Consider offering a discount to reduce churn risk due to high monthly charges.")
        if contract_type == 'Month-to-month':
            st.write("Offer a long-term contract (1-year or 2-year) to improve retention.")
        if tech_support == 'No':
            st.write("Provide access to tech support to increase customer satisfaction.")
        if online_security == 'No':
            st.write("Offer online security services to improve trust and retention.")
        if tenure < 12:
            st.write("Offer loyalty incentives to customers with shorter tenure to encourage them to stay longer.")
        if dependent == 'Yes':
            st.write("Since the customer has dependents, provide family-oriented services to increase retention.")
        if online_backup == 'No':
            st.write("Offer online backup services to enhance customer satisfaction and retention.")
    else:  # Customer predicted not to churn
        # Provide engagement strategies
        st.title("Advice to Enhance Customer Experience:")
        if monthly_charge > 80:
            st.write("Consider offering additional services to provide more value at a higher price point.")
        if tech_support == 'No':
            st.write("Encourage the customer to try tech support as an added benefit.")
        if online_security == 'No':
            st.write("Suggest online security services as an upgrade to improve their experience.")
        if tenure > 12:
            st.write("Loyal customer—consider offering exclusive rewards or VIP programs to enhance loyalty.")
