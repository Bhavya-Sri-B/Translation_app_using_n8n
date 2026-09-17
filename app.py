import streamlit as st
import requests

st.title(":rainbow[Welcome to Language Translation APP]")

text=st.text_area("Enter your text here: ")

if st.button("Hindi",key="Hindi_btn"):
    if text:
        response=requests.post(url="https://bhavya2608.app.n8n.cloud/webhook-test/f4f6349e-3e7b-4308-b8e4-63a512bee4e7",json={"input":text,"language":"Hindi"})
        if response.status_code==200:
            st.write(response.json()["text"])

elif st.button("Telugu",key="Telugu_btn"):
    if text:
        response=requests.post(url="https://bhavya2608.app.n8n.cloud/webhook-test/f4f6349e-3e7b-4308-b8e4-63a512bee4e7",json={"input":text,"language":"telugu"})
        if response.status_code==200:
            st.write(response.json()["text"])

else:
    pass