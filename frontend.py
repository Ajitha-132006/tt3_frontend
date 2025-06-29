import streamlit as st
import requests

API_URL = "https://tt3-backend.onrender.com"  # Replace with your FastAPI URL

st.title("📅 AI Appointment Booking Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask me to book an appointment...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    try:
        resp = requests.post(API_URL, json={"message": user_input})
        reply = resp.json()["reply"]
    except Exception as e:
        reply = f"Error contacting backend: {e}"
    st.session_state.chat_history.append(("ai", reply))

for role, msg in st.session_state.chat_history:
    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)
