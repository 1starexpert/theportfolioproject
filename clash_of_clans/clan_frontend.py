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
    st.image(clan_info[1])
    for line in clan_info[0]:
        st.write(line)




