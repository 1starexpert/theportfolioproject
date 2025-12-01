
import os
print("WORKING DIR:", os.getcwd())

import clan_backend
print("Backend imported successfully!")

import requests


import clan_backend


def textbox1():

    clan_tag = st.text_input("Enter a clan tag:")
    return clan_tag

textbox1()

"""
def textinput():

    clan_tag = input("Enter a valid clan tag: ")
    return clan_tag
"""

clan_backend.displayClanInformation(textbox1())
