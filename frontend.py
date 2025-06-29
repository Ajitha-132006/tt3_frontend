import streamlit as st
import requests

API_URL = "https://tt3-backend-1.onrender.com"  # Replace with your deployed FastAPI URL

st.title("📅 AI Calendar Booking Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# Chat input
user_input = st.chat_input("Ask me to book your event (e.g. Book lunch with Raj tomorrow at 2 PM)...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Send to backend
    try:
        resp = requests.post(API_URL, json={"message": user_input})
        if resp.status_code == 200:
            reply = resp.json().get("reply", "❌ No reply from backend.")
        else:
            reply = f"❌ Error: {resp.status_code} {resp.reason}"
    except Exception as e:
        reply = f"❌ Error contacting backend: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": reply})

    st.chat_message("assistant").write(reply)
