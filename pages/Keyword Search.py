import os
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
from rank_bm25 import BM25Okapi
import streamlit as st

from utils.commons import sidebar, font, top_space

st.set_page_config(layout = "wide", initial_sidebar_state = "collapsed", page_icon = "✧")

top_space()
font()
sidebar()

@st.cache_data
def get_text() -> dict:
    cases = {}
    tmp_case_data = pd.read_csv("data/New_2023.csv")
    for title, text in zip(tmp_case_data["Case Title"], tmp_case_data["Judgement Text"]):
        cases[title] = text
    return cases

def tokenize(text : str) -> list:
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    tokens = [token.lower() for token in tokens if token.isalnum() and token.lower() not in stop_words]
    return tokens

@st.cache_resource(show_spinner = False)
def create_bm25(file_contents):
    tokenized_corpus = [tokenize(content) for content in file_contents.values()]
    bm25 = BM25Okapi(tokenized_corpus)
    return bm25, tokenized_corpus

file_contents = get_text()
bm25, tokenized_corpus = create_bm25(file_contents)

if "total_cases" not in st.session_state:
    st.session_state.total_cases = file_contents

if "current_subset" not in st.session_state:
    st.session_state.current_subset = file_contents

def search_and_rank(bm25, file_contents, tokenized_corpus, search_term):
    tokenized_query = tokenize(search_term)
    doc_scores = bm25.get_scores(tokenized_query)
    current_indices = [list(st.session_state.total_cases.keys()).index(i) for i in file_contents]
    ranked_indices = sorted(range(len(doc_scores)), key = lambda i : doc_scores[i], reverse = True)
    intersection_cases = [i for i in current_indices if i in ranked_indices]
    ranked_files = [list(st.session_state.total_cases.keys())[i] for i in intersection_cases if doc_scores[i] > 0]
    return ranked_files, ranked_indices, doc_scores

def get_snippets(file : str, content : str, search_term : str) -> str:
    search_terms = search_term.split()
    snippet = ''
    for term in search_terms:
        match = re.search(r'(.{0,30}' + re.escape(term) + r'.{0,30})', content, re.IGNORECASE)
        if match:
            snippet = match.group(1)
            break
    return snippet if snippet else content[:200]

def display_results(file_contents, ranked_files, ranked_indices, doc_scores, search_term):
    for i, file in enumerate(ranked_files[:50]):
        snippet = get_snippets(file, file_contents[file], search_term)
        st.subheader(file)
        st.text(doc_scores[ranked_indices[i]])
        st.write("..." + snippet + "...")

if "queries" not in st.session_state:
    st.session_state.queries = []

if st.session_state.queries != []:
    if st.button("Clear Searches"):
        st.session_state.current_subset = file_contents
        st.session_state.queries = []
        st.rerun()

if st.session_state.queries != []:
    st.multiselect(label = "Search Subset - ", options = st.session_state.queries, default = st.session_state.queries, disabled = True)

if "run_search" not in st.session_state:
    st.session_state.run_search = False

query = st.text_input("Please input a search query -", value = "")

if query != "" and query not in st.session_state.queries:
    st.session_state.queries.append(query)
    st.session_state.run_search = True
    st.rerun()

if st.session_state.run_search:
    ranked_files, ranked_indices, doc_scores = search_and_rank(bm25, st.session_state.current_subset, tokenized_corpus, query)
    display_results(st.session_state.current_subset, ranked_files, ranked_indices, doc_scores, query)
    st.session_state.current_subset = {file : st.session_state.current_subset[file] for file in ranked_files}
    st.session_state.run_search = False