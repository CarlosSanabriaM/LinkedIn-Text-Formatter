import streamlit as st

# Function to apply unicode formatting
def apply_unicode_formatting(text, bold, italic, underline, strikethrough):
    if bold:
        text = ''.join([chr(ord('𝐀') + (ord(c) - ord('A'))) if 'A' <= c <= 'Z' else chr(ord('𝐚') + (ord(c) - ord('a'))) if 'a' <= c <= 'z' else c for c in text])
    if italic:
        text = ''.join([chr(ord('𝑨') + (ord(c) - ord('A'))) if 'A' <= c <= 'Z' else chr(ord('𝒂') + (ord(c) - ord('a'))) if 'a' <= c <= 'z' else c for c in text])
    if strikethrough:
        text = ''.join([c + '\u0336' for c in text])
    return text

# Streamlit app layout
st.title("LinkedIn Text Formatter")

text = st.text_area("Enter your text here:", height=150)

# Checkbox options for formatting
bold = st.checkbox("Bold")
italic = st.checkbox("Italic")
strikethrough = st.checkbox("Strikethrough")

# Apply formatting
formatted_text = apply_unicode_formatting(text, bold, italic, underline=False, strikethrough=strikethrough)

# Display formatted text
st.text_area("Formatted text (copy this):", formatted_text, height=150)
