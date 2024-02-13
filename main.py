import langchain_helper as lch
import streamlit as st

st.title("Pet Name Generator")

pet_type = st.sidebar.selectbox("What is your pet?", ("dog", "cat", "bird", "fish", "reptile"))

if pet_type:
    names_count = st.sidebar.slider("How many names do you want to generate?", 1, 10, 1)

if pet_type and names_count and st.button("Generate"):
    response = lch.generate_pet_name(pet_type, names_count)
    st.text(response["text"])
    st.text("Powered by OpenAI's GPT-3.5")
