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
    st.write("An innovative, enthusiastic individual looking for a responsible position to learn, grow and excel in new technologies.")
    st.write("[< learn more >](https://purnadandu.42web.io)")


with st.container():
    st.write("-----")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("what I want to do")
        st.write("##")
        st.write(
            """Wanted to be best in Machine Learning and build a best model for all data analysis
            """
        )

with right_column:
    st_lottie(lottie_coding,height=300,key="coding")


    with st.container():
        st.write("------")
        st.header("Experience")
        st.write("--Freelancer at UTest platform ")
        st.write("Enterpreuner at Meesho PVT LTD")
        
    
with st.container():
        st.write("------")
        st.header(" Technical-Skills")
        st.write("Languages : C, java, Python.")
        st.write("Problem Solving : DataStructures and Algorithms")
        st.write("Development : HTML, CSS, JS,Bootstrap, PHP, SQL")
        st.write("Databases : MySQL.")
        st.write("Additional Skills : Canva,wordpress")
        
        
with st.container():
    st.write("------")
    st.header("Certifications")
    st.write("[Data science](https://www.udemy.com/certificate/UC-ca3c1055-d568-45f5-8a6b-e2b1f4bfa27f/) -- Completed DataScience course from Udemy")
    st.write("[Wordpress](https://www.udemy.com/certificate/UC-7e692fa6-0ed8-46e0-80c0-a9df22825813/) -- Completed Wordpress basics course from Udemy")
    st.write("IBC hackathon Completion -- participated in IBC hackathon Organised in Hyderabad")
    st.write("Python Basics to Advanced -- By Perfect-E-Learning")
    st.write("Machine Learning -- By Perfect-E-Learning")
        
        



with st.container():
    st.write("------")
    st.header("contact me")
    st.write("##")
    



    





 



