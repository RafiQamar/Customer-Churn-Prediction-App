# Customer Churn Prediction

## Overview
This project is a Machine Learning-based web application built using Streamlit to predict customer churn. The model is trained on a dataset from IBM Sample Data Sets, which includes customer demographics, account information, and services used. The project aims to help businesses analyze customer behavior and develop focused retention strategies.

## Dataset Information
The dataset includes the following information:
- **Churn:** Whether a customer left within the last month.
- **Services Signed Up:** Phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming services.
- **Customer Account Information:** Tenure, contract type, payment method, paperless billing, monthly charges, and total charges.
- **Demographics:** Gender, age range, presence of partners, and dependents.

## Project Workflow
1. **Data Preprocessing:**
   - Handled missing values and inconsistencies in the dataset.
   - Encoded categorical variables using label encoding.
   - Standardized numerical features using a scaler.
   
2. **Model Training:**
   - Trained a Machine Learning model to predict customer churn.
   - Evaluated different models and selected the best-performing one.
   - Saved the trained model using `pickle` for deployment.
   
3. **Streamlit Application Development:**
   - Built an interactive user interface to accept customer details.
   - Integrated the trained model to make predictions based on user input.
   - Provided retention advice based on the model's output.

## Features
- **User Input Interface:** Users can input customer details to check if they are likely to churn.
- **Pre-trained Machine Learning Model:** The application uses a trained ML model to predict churn.
- **Advice System:** Provides recommendations to reduce churn risk or enhance customer experience.
- **Encoders and Scalers:** Uses `pickle` files for data transformation.
- **Retention Strategies:** If a customer is predicted to churn, the system suggests strategies to retain them.

## Usage
1. Open the web application.
2. Fill in customer details in the input form.
3. Click **Predict** to check if the customer is likely to churn.
4. Get personalized advice based on the prediction.

## Author
Rafi Qamar (GitHub: [RafiQamar](https://github.com/RafiQamar))


