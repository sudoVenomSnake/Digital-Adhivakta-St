import streamlit as st
from utils.commons import sidebar, font, top_space

st.set_page_config(layout = "wide", initial_sidebar_state = "collapsed", page_icon = "✧")

top_space()
font()
sidebar()

userData = [
    {'name': 'Swastik Gopalchandra Mishra', 'linkedin': 'https://www.linkedin.com/in/swastik-mishra26/?originalSubdomain=in','image': 'https://media.licdn.com/dms/image/D5603AQG1nto7GdgT0w/profile-displayphoto-shrink_800_800/0/1716652985173?e=1722470400&v=beta&t=e-d_AWgfGjuCgiOVQAdf7Q2xOTlIg_JRD4KeWgLZnQY', 'bio': 
     'Swastik Mishra is passionate about pursuing a career in technology and software development. He demonstrates a keen interest in leveraging innovative solutions to tackle complex challenges in the tech industry. With a strong foundation in programming languages and software development methodologies, Swastik is dedicated to continuous learning and staying updated with the latest advancements in technology.'
     },
    {'name': 'Tejas Madhukar','linkedin': 'https://www.linkedin.com/in/tejas-madhukar-b75554224/?originalSubdomain=in', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjcPiFKQF3Mztxv4u19aRlEUS-GfclMDeQsw1j8mEm9g&s', 'bio': 
     'Tejas Madhukar is driven by an unwavering enthusiasm for venturing into the realms of technology and software development. His fervor lies in exploring inventive approaches to address intricate issues prevalent in the tech sector. Equipped with a robust grasp of programming languages and adeptness in software development methodologies, Tejas exhibits a relentless commitment to ongoing education, ensuring he remains abreast of the cutting-edge innovations within the tech landscape.'
     },
    {'name': 'Tamish Sinha', 'linkedin': 'https://www.linkedin.com/in/tamish-sinha','image': 'https://media.licdn.com/dms/image/D4D03AQH4CzZwrdfrZQ/profile-displayphoto-shrink_800_800/0/1669274843278?e=1722470400&v=beta&t=57t5Tu6J7byrDBlfMctsHbKsXhhVEuciN5y4a819llI', 'bio': 
     'Tamish Sinha possesses an insatiable curiosity that propels him towards the ever-evolving landscape of technology and software development. His passion is deeply rooted in uncovering novel solutions to complex challenges within the tech industry. With a solid foundation in various programming languages and a keen understanding of software development frameworks, Tamish demonstrates an unwavering dedication to continuous learning, constantly seeking out the latest advancements and methodologies shaping the tech sphere.'
     }
]

def about_us_info():
    col1, col2 = st.columns([3,11])
    with col1:
        st.header(':grey[About Us]')
        st.markdown("<br>",unsafe_allow_html=True)

    with col2:
        st.markdown("<br>",unsafe_allow_html=True)
        st.markdown("[![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://www.github.com/judicial-junction)", unsafe_allow_html=True)


    for member in userData:
        st.markdown(
            f'<h3><a href="{member["linkedin"]}" target="_blank" style="text-decoration: none; color: grey;">{member["name"]}</a></h3>', 
            unsafe_allow_html=True
        )        
        st.write('')
        col1, col2 = st.columns([2, 3])
        with col1:
            st.markdown(f'<div style="display: flex; justify-content: center;"><img src="{member["image"]}" width="150" height="150"/></div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div style="display: flex; align-items: center; justify-content: center;">{member["bio"]}</div>', unsafe_allow_html=True)
        st.write('---')


about_us_info()
