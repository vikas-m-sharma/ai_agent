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

# import streamlit as st
# import requests
# import uuid

# # Initialize session
# if "session_id" not in st.session_state:
#     st.session_state.session_id = str(uuid.uuid4())[:8]
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # Sidebar options
# with st.sidebar:
#     st.text_input(
#         "Session ID:", value=st.session_state.session_id, disabled=True)
#     provider = st.radio("Model Provider:", ["Groq", "OpenAI"])
#     model = st.selectbox(
#         "Choose Model:",
#         ["llama-3.3-70b-versatile",
#             "mixtral-8x7b-32768"] if provider == "Groq" else ["gpt-4o-mini"]
#     )
#     system_prompt = st.text_area(
#         "AI Role Prompt:", height=80, placeholder="You're a helpful AI assistant.")
#     allow_search = st.checkbox("Enable Web Search", value=True)

# # Display chat
# for role, message in st.session_state.chat_history:
#     with st.chat_message(role):
#         st.markdown(message)

# # User input
# user_input = st.chat_input("Type your message...")

# if user_input:
#     st.session_state.chat_history.append(("user", user_input))
#     payload = {
#         "model_name": model,
#         "model_provider": provider,
#         "system_prompt": system_prompt,
#         "messages": [user_input],
#         "allow_search": allow_search,
#         "session_id": st.session_state.session_id
#     }

#     backend_url = "https://ai-agent-mqed.onrender.com/chat"  # Your Render backend URL
#     try:
#         response = requests.post(backend_url, json=payload)
#         if response.status_code == 200:
#             reply = response.json().get("response", "No response.")
#             st.session_state.chat_history.append(("assistant", reply))
#         else:
#             st.error(f"Error {response.status_code}: {response.text}")
#     except Exception as e:
#         st.error(f"Request failed: {e}")

# import streamlit as st
# import requests
# import uuid

# # -------------------------------
# # Initialize session
# # -------------------------------
# if "session_id" not in st.session_state:
#     st.session_state.session_id = str(uuid.uuid4())[:8]

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # -------------------------------
# # Sidebar options
# # -------------------------------
# with st.sidebar:
#     st.title("Inquiro AI")
#     st.caption("Your smart assistant for real-time, web-aware conversations.")
#     st.markdown("---")

#     # Display session ID
#     st.text_input(
#         "Session ID:", value=st.session_state.session_id, disabled=True)

#     # Reset chat
#     if st.button("Start New Chat"):
#         st.session_state.chat_history = []
#         st.session_state.session_id = str(uuid.uuid4())[:8]
#         st.experimental_rerun()

#     st.markdown("---")

#     # Model provider & selection
#     provider = st.radio("Model Provider:", ["Groq", "OpenAI"])
#     model = st.selectbox(
#         "Choose Model:",
#         ["llama-3.3-70b-versatile",
#             "mixtral-8x7b-32768"] if provider == "Groq" else ["gpt-4o-mini"]
#     )

#     # AI Role Prompt
#     system_prompt = st.text_area(
#         "AI Role Prompt:",
#         height=80,
#         placeholder="You're a helpful assistant with access to real-time knowledge."
#     )

#     # Web search toggle
#     allow_search = st.checkbox("Enable Web Search", value=True)

#     st.markdown("---")
#     st.markdown("Built by **Vikas Sharma**")

# # -------------------------------
# # Display chat history
# # -------------------------------
# for role, message in st.session_state.chat_history:
#     with st.chat_message(role):
#         st.markdown(message)

# # -------------------------------
# # User input
# # -------------------------------
# user_input = st.chat_input("Type your message here...")

# if user_input:
#     # Append user message to history
#     st.session_state.chat_history.append(("user", user_input))
#     with st.chat_message("user"):
#         st.markdown(user_input)

#     # Prepare payload
#     payload = {
#         "model_name": model,
#         "model_provider": provider,
#         "system_prompt": system_prompt,
#         "messages": [user_input],
#         "allow_search": allow_search,
#         "session_id": st.session_state.session_id
#     }

#     # Call live backend
#     backend_url = "https://ai-agent-mqed.onrender.com/chat"
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             try:
#                 response = requests.post(backend_url, json=payload)
#                 if response.status_code == 200:
#                     reply = response.json().get("response", "No response.")
#                     st.session_state.chat_history.append(("assistant", reply))
#                     st.markdown(reply)
#                 else:
#                     st.error(f"Error {response.status_code}: {response.text}")
#             except Exception as e:
#                 st.error(f"Request failed: {e}")

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from ai_agent import get_response_from_ai_agent
import os

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool
    session_id: str
    api_key: str = None   # Accept API key from frontend

ALLOWED_MODEL_NAMES = [
    "llama3-70b-8192",
    "mixtral-8x7b-32768",
    "llama-3.3-70b-versatile",
    "gpt-4o-mini"
]

app = FastAPI(title="Inquiro AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    try:
        # Check for valid model
        if request.model_name not in ALLOWED_MODEL_NAMES:
            return JSONResponse(
                content={"error": "Invalid model name. Kindly select a valid AI model."},
                status_code=status.HTTP_400_BAD_REQUEST
            )

        # Determine API key
        api_key = request.api_key if request.api_key else os.environ.get("GROQ_API_KEY", "")

        # If provider is Groq, ensure API key exists
        if request.model_provider.lower() == "groq" and not api_key:
            return JSONResponse(
                content={"error": "GROQ_API_KEY is missing. Please set it in environment or frontend."},
                status_code=status.HTTP_400_BAD_REQUEST
            )

        # Call AI agent safely
        response = get_response_from_ai_agent(
            llm_id=request.model_name,
            query=request.messages,
            allow_search=request.allow_search,
            system_prompt=request.system_prompt,
            provider=request.model_provider,
            session_id=request.session_id,
            api_key=api_key
        )

        return JSONResponse(content={"response": response}, status_code=200)

    except Exception as e:
        # Catch any unexpected error and return JSON instead of 500
        return JSONResponse(
            content={"error": f"Internal server error: {str(e)}"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
