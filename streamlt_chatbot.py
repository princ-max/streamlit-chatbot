from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
# from dotenv import load_dotenv
import os


# load_dotenv()

model = ChatOpenAI(model="gpt-4.1-mini", api_key=os.getenv("OPENAI_API_KEY"))

st.title("Prince Chatbot")

# store chat history

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# show old messages

for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        st.chat_message("user").write(message.content)
    elif isinstance(message, AIMessage):
        st.chat_message("assistant").write(message.content)



# User input

user_input = st.chat_input("type your message....")

if user_input:
    st.chat_message("user").write(user_input)

#save user message

    st.session_state.chat_history.append(HumanMessage(content=user_input))

# Get AI response

    result = model.invoke(st.session_state.chat_history)

#show AI response

    st.chat_message("assistant").write(result.content)

#send all history to model

    result=model.invoke(st.session_state.chat_history)

#save AI response

    st.session_state.chat_history.append(AIMessage(content=result.content))
