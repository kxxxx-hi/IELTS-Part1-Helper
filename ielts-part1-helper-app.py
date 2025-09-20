import streamlit as st
import streamlit.components.v1 as components

# Set a title and layout for the Streamlit app
st.set_page_config(page_title="IELTS Speaking Helper", layout="wide")

st.title("IELTS Speaking Test Part 1 Helper")

# Read the HTML file content
# NOTE: The HTML file (ielts_speaking_helper.html) must be in the same directory as this app.py file
try:
    with open("ielts_speaking_helper.html", "r", encoding="utf-8") as f:
        html_content = f.read()
except FileNotFoundError:
    st.error("Error: 'ielts_speaking_helper.html' not found. Please ensure the file is in the same directory.")
    html_content = ""

# Embed the HTML content using the Streamlit components API
if html_content:
    components.html(html_content, height=800, scrolling=True)

# You can add additional Streamlit elements below the HTML component if needed
st.markdown("---")
st.markdown("This application is powered by the Web Speech API and the Gemini API for feedback generation.")
