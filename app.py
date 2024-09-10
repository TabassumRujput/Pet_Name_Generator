import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate



load_dotenv()
genai.configure(api_key=os.environ["google_api_key"])

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.5)






template = ("Generate exactly 5 unique and cute pet names based on an animal {animal} and a color {color}."
            " Provide only the names, no additional explanation.Names display bulit format")


prompt_template = ChatPromptTemplate.from_template(template)

st.title("Pet Name Generator")


with st.sidebar:
    col1, col2 = st.columns(2)

    with col1:
        animal = st.selectbox("Animal Name", ["Dog", "Cat", "Elephant", "Lion", "Tiger", "Horse"])


    with col2:
        color = st.multiselect("Animal Color", ["Red", "Green", "Pink", "Blue", "White", "Black"])



if st.button("Generate Pet Name"):
    if animal and color:

        service_messages =prompt_template.format_messages(
            animal=animal,
            color=color
        )


        service_reply = service_messages


        pet_name = llm(service_reply)
        st.write("Generated Pet Names:")
        st.success(pet_name.content)
    else:
        st.error("Please enter both an animal and a color.")




