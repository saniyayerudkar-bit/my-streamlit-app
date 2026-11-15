import streamlit as st

st.title("My First Streamlit App")

st.write("Welcome to my Machine Learning Application!")

user_input = st.text_input("Enter your name or any text:")

if user_input:
    st.write("You entered:", user_input)
    st.success("Text displayed successfully!")

st.write("Created using Python and Streamlit")