import streamlit as st
import pickle
import numpy as np

st.title("addiction")

st.set_page_config(page_title="addiction", page_icon=":shark:", layout="wide")

def load_model():
    return pickle.load(open("linear_regression_model.pkl", "rb"))

model = load_model()

value1 = st.number_input("Hours spend on social media")
value2 = st.selectbox("Affects performace",[0,1])
st.write("you selected:",value2)
value3 = st.number_input("Sleep_Hours_Per_Night")
value4 = st.selectbox("Mental_Health_Score",[0,1,2,3,4,5,6,7,8,9,10])
st.write("you selected:",value4)
value5 = st.selectbox("Conflicts_Over_Social_Media",[0,1,2,3,4,5])
st.write("you selected:",value5)


if st.button("predict"):
    input_data = np.array([[value1, value2, value3, value4, value5]])
    prediction = model.predict(input_data)
    st.write(f"Predicted Addiction Level: {prediction[0][0]:.2f}")   



