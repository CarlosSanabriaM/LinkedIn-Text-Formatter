import streamlit as st

# Function to apply formatting
def apply_formatting(text, bold, italic, underline, strikethrough, superscript, subscript, color, size):
    if bold:
        text = f"**{text}**"
    if italic:
        text = f"*{text}*"
    if underline:
        text = f"<u>{text}</u>"
    if strikethrough:
        text = f"~~{text}~~"
    if superscript:
        text = f"<sup>{text}</sup>"
    if subscript:
        text = f"<sub>{text}</sub>"
    if color:
        text = f'<span style="color:{color};">{text}</span>'
    if size:
        text = f'<span style="font-size:{size}px;">{text}</span>'
    return text

# Streamlit app layout
st.title("LinkedIn Text Formatter")

text = st.text_area("Enter your text here:", height=150)

# Checkbox options for formatting
bold = st.checkbox("Bold")
italic = st.checkbox("Italic")
underline = st.checkbox("Underline")
strikethrough = st.checkbox("Strikethrough")
superscript = st.checkbox("Superscript")
subscript = st.checkbox("Subscript")

# Color picker and font size slider
color = st.color_picker("Pick a text color", "#000000")
size = st.slider("Font size", 10, 50, 14)

# Apply formatting
formatted_text = apply_formatting(text, bold, italic, underline, strikethrough, superscript, subscript, color, size)

# Display formatted text
st.markdown("### Formatted text:")
st.markdown(formatted_text, unsafe_allow_html=True)

# Copy to clipboard (additional feature)
st.code(formatted_text, language='html')
