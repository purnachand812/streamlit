from cgitb import text
from json import load
from os import link
from click import style
from nbformat import write
import requests
import streamlit as st
from streamlit_lottie import st_lottie



st.set_page_config(page_title="my webpage",page_icon=":tada:",layout="wide")


def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


def local_css(file_name):
        with open(file_name) as f:
             st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style/style.css")



lottie_coding= load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_ngzwzxib.json")


with st.container():
    st.subheader("hi im purnachand :wave:")
    st.title("student from india")
    st.write("i ma passionate about learning new things about tech and i try to build new things using python and another languages")
    st.write("[< learn more >](https://purnadandu.42web.io)")


with st.container():
    st.write("-----")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("what I want to do")
        st.write("##")
        st.write(
            """
            i just want to be successfull web developer 
            """
        )

with right_column:
    st_lottie(lottie_coding,height=300,key="coding")


    with st.container():
        st.write("------")
        st.header("my progress")
        st.write("i have completed my python basic and python data structures courses ")
        
    



with st.container():
    st.write("------")
    st.header("contact me")
    st.write("##")


    contact_form = """
    <form action="https://formsubmit.co/purnachand0812@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" palceholder="your name" required>
     <input type="email" name="email" placeholder="your email" required>
     <textarea name ="message"placeholder=""write your message">
     <button type="submit">Send</button>
</form>
"""

left_column,right_column=st.columns(2)
with left_column:
    st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
    st.empty()


    





 



