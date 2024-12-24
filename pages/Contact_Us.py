import streamlit as st
from send_emails import send_email

st.title("Contact Us") # Adding the title of the page



with st.form("contact_us"):                      # creating the streamlit form with name inside ""
    user_email = st.text_input("Provide your email address:") # Adding a line of text with label "Label inside"
    user_message = st.text_area("Write your Message:")          # Adding a text area with label "Label inside"
    message =  f"""\
Subject: From user {user_email}

From: {user_email}

{user_message }"""
    button =st.form_submit_button("Submit")      # Adding form submit button with label "Label inside"
    if button:
        send_email(message)
        st.info("Message sent successfully")
