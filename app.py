import streamlit as st
import requests

# FastAPI endpoint
API_URL = "http://127.0.0.1:8000/translate"

st.set_page_config(page_title="Egy→Eng Translator", page_icon="🌍")
st.title("🌍 Egyptian Arabic → English Translator")

st.markdown("Enter **Egyptian Arabic** text below and get an English translation.")

# User input
user_input = st.text_area("✍️ Write something in Egyptian Arabic:", height=150)

if st.button("Translate"):
    if not user_input.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        with st.spinner("Translating..."):
            try:
                # Send POST request to FastAPI backend
                response = requests.post(API_URL, json={"text": user_input})
                if response.status_code == 200:
                    translation = response.json()["translation"]
                    st.success("✅ Translation complete!")
                    st.markdown(f"**English:** {translation}")
                else:
                    st.error(f"❌ Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"🚨 Failed to connect to API: {e}")
