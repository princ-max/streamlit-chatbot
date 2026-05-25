import streamlit as st 
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
if "message" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("type your message")

if prompt:
    st.session_state.message.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.write(prompt)
        
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=st.session_state.messages
    )
    reply = response.choices[0].message.content

    st.session_state.message.append({"role":"user","content":reply})

    with st.chat_message("assistant"):
        st.write(reply)