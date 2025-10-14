from dotenv import load_dotenv
load_dotenv()

import os
from openai import OpenAI
import streamlit as st
import google.generativeai as genai

# Get Gemini API key from .env
api_key = os.environ.get("GEMINI_API_KEY")

# Configure the Gemini client
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("Simple Sentiment Analysis App (Gemini)")

user_input = st.text_area("Enter text to analyze sentiment")

if st.button("Analyze"):
    if user_input.strip():
        # Prompt Gemini for sentiment analysis
        prompt = f"Is the sentiment of this text Positive, Negative, or Neutral? Text: '{user_input}'. Respond with only one word."
        response = model.generate_content([prompt])
        st.write(f"Sentiment: **{response.text.strip()}**")
    else:
        st.write("Please enter some text to analyze.")