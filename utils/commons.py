import streamlit as st
from st_pages import Page, show_pages, hide_pages

def top_space() -> None:
    st.markdown(
    """
        <style>
            .appview-container .main .block-container {{
                padding-top: {padding_top}rem;
                padding-bottom: {padding_bottom}rem;
                }}

        </style>""".format(
        padding_top = 1, padding_bottom = 1
        ),
        unsafe_allow_html=True,
    )

def font() -> None:
    streamlit_style = """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Maven+Pro:wght@400..900&display=swap');

            body * {
                font-family: "Maven Pro", sans-serif, sans-serif !important;
            }
        </style>
    """
    st.write(streamlit_style, unsafe_allow_html = True)

def sidebar() -> None:
    show_pages(
        [
            Page("Home.py", "Home", "🏠"),
            Page("pages/About Us.py", "About Us", ":books:"),
            Page("pages/Keyword Search.py", "Keyword Search", "🔠", in_section = True),
            Page("pages/Sentence Similarity.py", "Sentence Similarity", "🔢", in_section = True),
            Page("pages/case_chat.py", "case_chat")
        ]
    )
    hide_pages(["case_chat"])