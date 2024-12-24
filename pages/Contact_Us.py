import streamlit as st

st.title("Contact Us") # Adding the title of the page



with st.form("contact_us"):                      # creating the streamlit form with name inside ""
    st.text_input("Provide your email address:") # Adding a line of text with label "Label inside"
    st.text_area("Write your Message:")          # Adding a text area with label "Label inside"
    button =st.form_submit_button("Submit")      # Adding form submit button with label "Label inside"
    if button:
        print("Message sent")
