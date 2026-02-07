import streamlit as st
import requests

st.title("🛒 Amazon Product Rating Prediction")

st.write("Enter product details to predict rating")

# Inputs
discounted_price = st.number_input("Discounted Price", min_value=0.0)
actual_price = st.number_input("Actual Price", min_value=0.0)
discount_percentage = st.number_input("Discount Percentage", min_value=0.0, max_value=100.0)
rating_count = st.number_input("Rating Count", min_value=0.0)

# Predict Button
if st.button("Predict Rating"):

    data = {
        "discounted_price": discounted_price,
        "actual_price": actual_price,
        "discount_percentage": discount_percentage,
        "rating_count": rating_count
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        result = response.json()

        st.success(f"⭐ Predicted Rating: {result['predicted_rating']:.2f}")

    except:
        st.error("API not running. Start FastAPI first.")

