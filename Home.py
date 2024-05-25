import streamlit as st
from streamlit_lottie import st_lottie
from st_click_detector import click_detector
import time
import base64

from utils.commons import sidebar, font, top_space

st.set_page_config(layout = "wide", initial_sidebar_state = "collapsed", page_icon = "✧")

top_space()
font()
sidebar()

def get_base64_of_bin_file(bin_file : bytes) -> str:
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

if "not_loaded_home" not in st.session_state:
    st.session_state.not_loaded_home = False

_, col, _ = st.columns([1, 3, 1])

if not st.session_state.not_loaded_home:
    with col:
        st_lottie(st.secrets["LOGO"], height = 500, loop = False)
    time.sleep(3)
    st.session_state.not_loaded_home = True
    st.rerun()

with col:
    st.title(":grey[Welcome to] Digital Adhivakta ✧")

col1, col2, col3, col4 = st.columns(4)

with col1:
    content = f"""
    <a href='#' id='Image 1'><img width='100%' src='data:image/png;base64,{get_base64_of_bin_file("assets/Keyword Search.png")}'></a>
    """
    clicked = click_detector(content)
    if clicked:
        st.switch_page('pages/Keyword Search.py')

with col2:
    content = f"""
    <a href='#' id='Image 2'><img width='100%' src='data:image/png;base64,{get_base64_of_bin_file("assets/Sentence Similarity.png")}'></a>
    """
    clicked = click_detector(content)
    if clicked:
        st.switch_page('pages/Sentence Similarity.py')

# with col3:
#     st.subheader('Consumer Trends')
#     content = f"""
#     <a href='#' id='Image 3'><img width='100%' src='data:image/png;base64,{get_base64_of_bin_file("assets/Keyword Search.png")}'></a>
#     """
#     clicked = click_detector(content)
#     if clicked:
#         st.switch_page('consumer trends')

# with col4:
#     st.subheader('The Triage')
#     content = f"""
#     <a href='#' id='Image 4'><img width='100%' src='data:image/png;base64,{get_base64_of_bin_file("assets/Keyword Search.png")}'></a>
#     """
#     clicked = click_detector(content)
#     if clicked:
#         st.switch_page('triage')

# st.write("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean in imperdiet nunc. Fusce pharetra libero ac tellus vehicula pretium. Duis maximus imperdiet convallis. Aliquam fermentum ullamcorper ex ac accumsan. Fusce id dictum mauris. Nunc at accumsan tellus, vel sollicitudin mi. Aenean nec orci at felis condimentum mattis sit amet ut ipsum.

# Aliquam in leo nec elit maximus feugiat. Fusce lacus lacus, vestibulum ac dui dignissim, rutrum viverra erat. Pellentesque consectetur eros vel mattis sollicitudin. Curabitur sed vehicula enim. Curabitur mollis urna nec ex sodales, et elementum turpis placerat. Phasellus quis pharetra neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Pellentesque turpis augue, dignissim in sem mattis, molestie auctor purus. Duis mollis vestibulum bibendum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus tempor risus id laoreet ultrices. Mauris sagittis mauris vel ullamcorper vulputate. Ut viverra quis orci eu accumsan. Aliquam erat volutpat. Proin id egestas turpis, id placerat leo.

# Suspendisse posuere erat eu turpis aliquam, sed pretium lacus efficitur. Vivamus interdum maximus nisl, vel dignissim neque vulputate et. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse ac magna a velit pharetra venenatis. Aliquam malesuada laoreet metus at mattis. Mauris accumsan tempus ultrices. Donec tincidunt, ante a porta mollis, orci mauris iaculis neque, sit amet vulputate massa massa in mi. Aliquam erat volutpat. Phasellus ac placerat orci. Suspendisse a metus commodo, euismod diam id, posuere nunc. Quisque sagittis felis sit amet nulla posuere pulvinar. Nullam at libero vel lacus sagittis viverra.

# Aenean neque dui, rutrum a accumsan a, vehicula sed ligula. Donec pretium venenatis ante, nec accumsan dolor congue eu. Donec convallis elementum est, vel ultricies libero scelerisque ut. In sagittis porta sodales. Sed ut diam nec est egestas tincidunt. Mauris ornare, elit vel mollis dictum, ligula erat rutrum justo, ut pulvinar magna lectus sit amet lectus. Cras tincidunt blandit est eget sollicitudin.

# Maecenas ultricies urna metus, vitae venenatis felis condimentum sit amet. Sed id est mollis, gravida sapien ut, imperdiet tellus. Morbi nulla justo, porttitor nec velit non, efficitur tincidunt nunc. Nulla id turpis sed arcu cursus ultrices nec gravida lacus. Curabitur fringilla magna nec sagittis ullamcorper. Maecenas blandit neque sed risus convallis, a tempor urna vulputate. Mauris scelerisque in mi sit amet pellentesque. Nullam nec urna congue, semper sem sit amet, facilisis ante. Integer laoreet in ex non sollicitudin. Vivamus sollicitudin vel neque eget ornare. Duis quis iaculis ligula, id mollis eros. Suspendisse accumsan rhoncus lorem, id mattis mauris ultricies vitae. Quisque blandit orci sapien, vel rutrum augue congue vel. Sed vehicula malesuada nisl, ut elementum est feugiat sed.""")