import streamlit as st
import requests
import json

def join_list(elements):
    if not elements:
        return ""  # Return an empty string for an empty list
    elif len(elements) == 1:
        return elements[0]  # Return the single element
    else:
        return " or ".join(elements)  # Join with comma for multiple elements

def get_recommended_sizes(gender, age, weight, height):
    """
    Function to send a request to the backend and get the recommended sizes.
    """
    user_input = {
        "gender": gender,
        "age": float(age),
        "weight": float(weight),
        "height": float(height * 10)  # Convert height from cm to mm if necessary
    }
    try:
        # Change URL to match your backend service
        # Cloud run endpoint
        res = requests.get("https://body-size-pred-6xm4os3l7a-an.a.run.app/predict", params=user_input)
        # res = requests.get("http://backend:8000/predict", params=user_input)

        if res.status_code == 200:
            res_json = res.json()
            tops = res_json['rec_size']['top_size']
            bottoms = res_json['rec_size']['bottom_size']
            return tops, bottoms
        else:
            st.error(f"Error: {res.status_code} - {res.text}")
            return None, None
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None, None


# Streamlit app
st.title(':red[UNIQLO] size recommender :shirt:')

# Get gender
gender = st.selectbox(
    "What's your gender?",
    ("M", "F"))

# Get age
age = st.number_input("Input your age", min_value=0, max_value=120, step=1)

# Get weight
weight = st.number_input("Input your weight(kg)", min_value=0.0, max_value=300.0, step=0.1)

# Get height
height = st.number_input("Input your height(cm)", min_value=0.0, max_value=250.0, step=0.1)

# Submit/send post requests
if st.button("Get sizes"):
    tops, bottoms = get_recommended_sizes(gender, age, weight, height)
    if tops and bottoms:
        st.info(f"Recommended size for tops: {join_list(tops)} and for bottoms: {join_list(bottoms)}")


