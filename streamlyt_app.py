from cgitb import text
from json import load
from os import link
from click import style
import requests
import streamlit as st



st.set_page_config(page_title="my webpage",page_icon=":tada:",layout="wide")


def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()


def local_css(file_name):
        with open(file_name) as f:
             st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)


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

    
    
    
    /* Style inputs with type="text", select elements and textareas */
input[type=text], input[type=email], textarea {
  width: 100%; /* Full width */
  padding: 12px; /* Some padding */ 
  border: 1px solid #ccc; /* Gray border */
  border-radius: 4px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 6px; /* Add a top margin */
  margin-bottom: 16px; /* Bottom margin */
  resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
}

/* Style the submit button with a specific background color etc */
input[type=submit] {
  background-color: #04AA6D;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

/* When moving the mouse over the submit button, add a darker green color */
input[type=submit]:hover {
  background-color: #45a049;
}


    





 



