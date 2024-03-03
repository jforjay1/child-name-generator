import streamlit as st
import os
#from secretkey import api_key
from openai import OpenAI
os.environ["OPENAI_API_KEY"]= st.secrets["api_key"] #replace with api_key if running locally
client = OpenAI()

def generate(name1,name2):
    user_content =f"name1={name1},name2={name2}"
    completion = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:personal::8yMG6PWl",
        messages=[
            {"role": "system", "content": "You are an astrology guru who have mastered in suggesting names for the new born children. You can combine two names and generate two meaningful names for a boy and a girl."},
            {"role": "user", "content": f"{user_content}"}
        ]
        )
    return completion.choices[0].message.content

st.title("Child Name Generator")
name1 = st.text_input("Dad's Name")
name2 = st.text_input("Mom's Name")

st.button("Reset", type="primary")
if st.button("Submit"):
    output = generate(name1,name2)
    st.subheader("Output:")
    st.write(output)

