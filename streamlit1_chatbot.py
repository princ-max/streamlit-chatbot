from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import initialize_agent, AgentType
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
#from dotenv import load_dotenv
import os


#load_dotenv()

TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    api_key=OPENAI_API_KEY
)

search = TavilySearchResults(max_results=3, tavily_api_key=TAVILY_API_KEY)

tools=[search]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

st.title("Prince chatbot with web search")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        st.chat_message("user").write(message.content)
    elif isinstance(message, AIMessage):
        st.chat_message("assistant").write(message.content)

user_input = st.chat_input("Type your message...")

if user_input:
    st.chat_message("user").write(user_input)

    st.session_state.chat_history.append(HumanMessage(content=user_input))

    response = agent.run(user_input)

    st.chat_message("assistant").write(response)

    st.session_state.chat_history.append(AIMessage(content=response))

