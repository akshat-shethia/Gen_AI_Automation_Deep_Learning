from dotenv import find_dotenv, load_dotenv

import streamlit as st
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def gemini_get_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title = 'Q&A DEMO')

input = st.text_input("Enter your Question: ", key = "input")
button = st.button("Ask the Question: ")

if button:
    response = gemini_get_response(input)
    st.subheader("The Response is: ")
    st.write(response)
    