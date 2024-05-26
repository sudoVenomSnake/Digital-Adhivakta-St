import streamlit as st
import requests
from requests.exceptions import RequestException

from utils.commons import sidebar, font, top_space

st.set_page_config(layout = "wide", initial_sidebar_state = "collapsed", page_icon = "✧")

top_space()
font()
sidebar()

@st.cache_data
def sentence_search_mutation(input_str : str) -> dict:
    embedding_server_host = st.secrets["EMBEDDING_ENDPOINT"]
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    data = {
        "message": input_str,
    }
    url = f"http://{embedding_server_host}:8000/sentence_similarity"
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        results = response.json()
        for result in results:
            result['search_type'] = "Sentence Similarity"
            result['search_query'] = input_str
        return results
    except RequestException as error:
        print(error)
        raise RuntimeError("Connection to embeddings-conversion server failed")

query = st.text_input("Please put in your input query -")

if query:
    for n_, i in enumerate(sentence_search_mutation(query)):
        st.subheader(f"""[{i["fields"]["Case Title"][0]}]({i["fields"]["Judgement PDF URL"][0]})""")
        st.text(i["fields"]["Case Number"][0])
        try:
            st.markdown(" ".join(["**" + i.strip() + "**" if n == 2 else i for n, i in enumerate(i["fields"]["Sentences"])]))
        except:
            pass
        st.text(i["fields"]["Judgement Date"][0])
        if st.button("💬 Chat With Judgement", key = i["fields"]["Case Title"][0] + f"_{n_}"):
            if "messages" in st.session_state:
                del st.session_state.messages
            st.session_state.case_selected = i["fields"]["Case Title"][0]
            st.switch_page("pages/Case Chat.py")