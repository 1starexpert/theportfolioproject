#import clan_backend
print("Backend imported successfully!")

import requests

import streamlit as st



def textbox1():

    clan_tag = st.text_input("Enter a clan tag:")
    return clan_tag
