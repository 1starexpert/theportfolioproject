
import google.generativeai as genai
import os
import requests as rq
import streamlit as st



genai.configure(api_key="AIzaSyDWmEC7nfCEw_b2QL48yZ2ByVq1QGBtBos")

model = genai.GenerativeModel("gemini-1.5-flash") #this is the free model of google gemini
#response = model.generate_content("Write a poem about how learning web development is fun!") #enter your prompt here!

#print(response.text) #dont forget to print your response!

try:
    
    response1 = rq.get('https://potterapi-fedeperin.vercel.app/en/spells')
    spells = response1.json()
    response2 = rq.get('https://potterapi-fedeperin.vercel.app/en/characters')
    characters = response2.json()
except:

    st.write("Unfortunately the API is not responding at the moment. Please try again later. 😔")
    


response = model.generate_content(f"Go through this list containing dictionaries of Harry Potter Spells : {spells} and list out each one with commas in between. Sort it by alphabetical order") #enter your prompt here!
second_response = model.generate_content(f"{characters} provided is a list of dictionaries containing characters in Harry Potter. Parse through that and take note of the characters.")
#print(response.text)

##### Website



def maintext():

    st.title("Dueling Simulator:")

    

    st.subheader("⚡️Choose two of the following spells below⚡️:️")

    st.write(response.text)

maintext()

def textbox():
    character1 = st.text_input("Enter the name of first spell")
    return(character1)
spell1 = textbox()
    




def textbox1():

    spell1 = st.text_input("Enter the name of the second spell.")
    return(spell1)

spell2 = textbox1()



responseA = model.generate_content(f"{spell1} is the name of the first spell selected. {spell2} is the name of the second spell selected. If two duelists had equally skill and dueled each other, one of them using spell1, and the other using spell2, predict who would win. Do not say inconclusive. As long as spell1 and spell2 are spells in {spells}, return duel results.")

                                   

st.subheader("Duel Results:")
st.write(responseA.text)

x = st.sidebar.text_input("Questions? Ask Google Gemini?")

chat_response = model.generate_content(f"Respond to this question or chat conservation:{x}about any questions the user may have about Harry Potter or spells in Harry Potter")

try:
    st.sidebar.write(chat_response.text)
except:
    st.sidebar.write("Whoops! Error! You may have reached the rate limit for the API or accidentally tried to generate something inappropiate. Please try again later!")






    
    


    
    




