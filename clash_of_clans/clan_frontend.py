import streamlit as st
import os
print("WORKING DIR:", os.getcwd())

import clan_backend
print("Backend imported successfully!")

import requests


import clan_backend


st.title("Clash of Clans Clan Info")

# Get the user input
clan_tag = st.text_input("Enter a clan tag:")

# Only call backend if the user entered something
if clan_tag:
    clan_info = clan_backend.displayClanInformation(clan_tag)
    for line in clan_info:
        st.write(line)


"""
def textinput():

    clan_tag = input("Enter a valid clan tag: ")
    return clan_tag


print(clan_backend.displayClanInformation(textinput()))
"""

