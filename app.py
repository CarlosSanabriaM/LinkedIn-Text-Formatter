import streamlit as st
import pyperclip

st.title("LinkedIn Text Formatter")

# Input text area
input_text = st.text_area("Enter your text here:")

# Formatting options
bold = st.checkbox("Bold")
italic = st.checkbox("Italic")

# Format the text based on options
formatted_text = input_text
if bold:
    formatted_text = f"**{formatted_text}**"
if italic:
    formatted_text = f"*{formatted_text}*"

# Display formatted text
st.subheader("Formatted Text Preview")
st.markdown(formatted_text)

# Copy text button
if st.button("Copy Text"):
    pyperclip.copy(formatted_text)
    st.success("Text copied to clipboard!")

# Clear button
if st.button("Clear"):
    st.experimental_rerun()
