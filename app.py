from openai import OpenAI
import streamlit as st

file = open("keys/.api_key")
key = file.read()

client = OpenAI(api_key=key)

st.title("👩‍💻AI Driven Code Reviewer")
st.subheader("Find the errors in your code and get the correct code.")

prompt = st.text_area("Type your code here..")

if st.button("Review"):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a debugger of python code. Find out the errors in the python code and display the error and correction of code in a userfriendly manner"},
            {"role": "user", "content": prompt}
        ]
    )
    st.write(response.choices[0].message.content)
