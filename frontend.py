# import streamlit as st
# import requests
# import uuid

# st.set_page_config(page_title="Inquiro AI", layout="wide")

# if "session_id" not in st.session_state:
#     st.session_state.session_id = str(uuid.uuid4())[:8]

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# with st.sidebar:
#     st.markdown(" Inquiro AI")
#     st.caption("Your smart assistant for real-time, web-aware conversations.")
#     st.markdown("---")

#     st.text_input("Session ID:", value=st.session_state.session_id,
#                   key="session_id_display", disabled=True)

#     if st.button(" Start New Chat"):
#         st.session_state.chat_history = []
#         st.session_state.session_id = str(uuid.uuid4())[:8]
#         st.rerun()

#     st.markdown("---")

#     provider = st.radio("Model Provider:", ["Groq", "OpenAI"])
#     model = st.selectbox(
#         "Choose Model:",
#         ["llama-3.3-70b-versatile",
#             "mixtral-8x7b-32768"] if provider == "Groq" else ["gpt-4o-mini"]
#     )

#     system_prompt = st.text_area(
#         " AI Role Prompt:",
#         height=80,
#         placeholder="You're a helpful assistant with access to real-time knowledge."
#     )

#     allow_search = st.checkbox(" Enable Web Search", value=True)

#     st.markdown("---")
#     st.markdown("Built by **Vikas Sharma**")

# for role, message in st.session_state.chat_history:
#     with st.chat_message("user" if role == "user" else "assistant"):
#         st.markdown(message)

# user_input = st.chat_input("Type your message here...")

# if user_input:
#     if user_input.lower().strip() in ["hi", "hello", "hey", "how are you?", "good morning", "good evening"]:
#         allow_search = False

#     st.session_state.chat_history.append(("user", user_input))
#     with st.chat_message("user"):
#         st.markdown(user_input)

#     payload = {
#         "model_name": model,
#         "model_provider": provider,
#         "system_prompt": system_prompt,
#         "messages": [user_input],
#         "allow_search": allow_search,
#         "session_id": st.session_state.session_id
#     }

#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             try:
#                 response = requests.post(
#                     "http://127.0.0.1:9999/chat", json=payload)

#                 if response.status_code == 200:
#                     reply = response.json().get("response", "No response.")
#                     st.session_state.chat_history.append(("assistant", reply))
#                     st.markdown(reply)
#                 else:
#                     st.error(f"Error {response.status_code}: {response.text}")
#             except Exception as e:
#                 st.error(f"Request failed: {e}")

import streamlit as st
import requests
import uuid

# Initialize session
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())[:8]
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar options
with st.sidebar:
    st.text_input(
        "Session ID:", value=st.session_state.session_id, disabled=True)
    provider = st.radio("Model Provider:", ["Groq", "OpenAI"])
    model = st.selectbox(
        "Choose Model:",
        ["llama-3.3-70b-versatile",
            "mixtral-8x7b-32768"] if provider == "Groq" else ["gpt-4o-mini"]
    )
    system_prompt = st.text_area(
        "AI Role Prompt:", height=80, placeholder="You're a helpful AI assistant.")
    allow_search = st.checkbox("Enable Web Search", value=True)

# Display chat
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    payload = {
        "model_name": model,
        "model_provider": provider,
        "system_prompt": system_prompt,
        "messages": [user_input],
        "allow_search": allow_search,
        "session_id": st.session_state.session_id
    }

    backend_url = "https://ai-agent-mqed.onrender.com/chat"  # Your Render backend URL
    try:
        response = requests.post(backend_url, json=payload)
        if response.status_code == 200:
            reply = response.json().get("response", "No response.")
            st.session_state.chat_history.append(("assistant", reply))
        else:
            st.error(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"Request failed: {e}")
