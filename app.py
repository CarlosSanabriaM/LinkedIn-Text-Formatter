import streamlit as st

# Function to apply basic LinkedIn-compatible formatting
def apply_formatting(text, bold, italic):
    if bold:
        text = f"**{text}**"  # Markdown for bold
    if italic:
        text = f"*{text}*"  # Markdown for italic
    return text

# Streamlit app layout
st.title("LinkedIn Text Formatter")

text = st.text_area("Enter your text here:", height=150)

# Checkbox options for formatting
bold = st.checkbox("Bold")
italic = st.checkbox("Italic")

# Apply formatting
formatted_text = apply_formatting(text, bold, italic)

# Display formatted text
st.markdown("### Formatted text:")
st.write(formatted_text)

# Instructions for LinkedIn
st.markdown("**Instructions for LinkedIn:**")
st.markdown("LinkedIn supports basic Markdown formatting:")
st.markdown("- Use `**text**` for bold")
st.markdown("- Use `*text*` for italics")
st.markdown("Note: LinkedIn does not support underlining, strikethroughs, colors, or font size adjustments.")
