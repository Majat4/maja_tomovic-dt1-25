import streamlit as st
import requests
import os

st.title("A Simple Chat System")

# Get backend URL from environment
BASE_URI = os.environ.get("BASE_URI")

if not BASE_URI:
    st.error("❌ BASE_URI is missing. Backend API cannot be reached.")
    st.stop()

st.write("Ask me something")

user_input = st.text_input("")

if st.button("chat"):
    try:
        endpoint = f"{BASE_URI}/chat"
        params = {
            "model_id": "deepseek/deepseek-chat-v3.1:free",
            "input": user_input
        }

        response = requests.get(endpoint, params=params)

        if response.status_code != 200:
            st.error(f"Backend error ({response.status_code}): {response.text}")
        else:
            data = response.json()
            st.success(data.get("ack", "No response"))
    except Exception as e:
        st.error(f"Request failed: {e}")
