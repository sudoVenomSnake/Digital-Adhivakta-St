import pandas as pd
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key = st.secrets['OPENAI_API_KEY'])

from utils.commons import sidebar, font, top_space

st.set_page_config(layout = "wide", initial_sidebar_state = "collapsed", page_icon = "✧")

top_space()
font()
sidebar()

@st.cache_data
def get_case_data() -> pd.DataFrame:
    return pd.read_csv("data/New_2023.csv")

data = get_case_data()
languages = ["English", "Assamese", "Bengali", "Bodo", "Dogri", "Gujarati", "Hindi", "Kannada", "Kashmiri", "Konkani", "Maithili", "Malayalam", "Manipuri (Meitei)", "Marathi", "Nepali", "Odia", "Punjabi", "Sanskrit", "Santali", "Sindhi", "Tamil", "Telugu", "Urdu"]

language = st.selectbox(label = "Please select a language you want answers in - ", options = languages, index = 0)

if "case_selected" not in st.session_state:
    case_choice = st.selectbox(label = "Select a case - ", options = data["Case Title"], index = None)
    if case_choice is not None:
        st.session_state.case_selected = case_choice
        st.rerun()

if "case_selected" in st.session_state:
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append({"role": "user", "content": f"I will ask you questions on this judgement - \n{data[data["Case Title"] == st.session_state.case_selected].values[0]}"})
    for message in st.session_state.messages[1:]:
        with st.chat_message(message["role"]):
            if message["role"] == "user":
                st.markdown(message["content"].split("*#&")[1])
            else:
                st.markdown(message["content"])
    prompt = st.chat_input()
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            report = []
            st.session_state.messages.append({"role" : "user", "content" : f"&#* Answer the prompt in {language} *#&\n" + prompt})
            for resp in client.chat.completions.create(
                model = "gpt-4o",
                messages = st.session_state.messages,
                stream = True):
                if resp.choices[0].finish_reason == "stop":
                    break
                full_response += resp.choices[0].delta.content
                report.append(resp.choices[0].delta.content)
                result = "".join(report).strip()  
                message_placeholder.markdown(f'{result}' + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})