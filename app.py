import streamlit as st

# Function to apply formatting
def apply_formatting(text, bold, italic, underline, strikethrough):
    if bold:
        text = f"**{text}**"
    if italic:
        text = f"*{text}*"
    if underline:
        text = f"_{text}_"
    if strikethrough:
        text = f"~~{text}~~"
    return text

# Streamlit app layout
st.title("LinkedIn Text Formatter")

text = st.text_area("Enter your text here:", height=150)

# Checkbox options for formatting
bold = st.checkbox("Bold")
italic = st.checkbox("Italic")
underline = st.checkbox("Underline")
strikethrough = st.checkbox("Strikethrough")

# Apply formatting
formatted_text = apply_formatting(text, bold, italic, underline, strikethrough)

# Display formatted text
st.markdown("### Formatted text:")
st.write(formatted_text)

# Instructions for LinkedIn
st.markdown("**Instructions for LinkedIn:**")
st.markdown("LinkedIn supports basic Markdown formatting:")
st.markdown("- Use `**text**` for bold")
st.markdown("- Use `*text*` for italics")
st.markdown("- Use `~~text~~` for strikethrough")
st.markdown("- Underline is not supported in LinkedIn posts")
