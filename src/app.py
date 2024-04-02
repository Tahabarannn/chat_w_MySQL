from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.set_page_config(page_title="Chat with MySQL", page_icon=":speech_balloon:")

st.title("Chat with MySQL")

with st.sidebar:
    st.subheader("Settings")
    st.write("This is a chat application that uses MySQL as a backend. Connect to the database and start chatting.")

    st.text_input("Host", value="localhost")
    st.text_input("Port", value="3306")
    st.text_input("User", value="root")
    st.text_input("Password", type="password", value="admin")
    st.text_input("Database", value="chat")

    st.button("Connect")