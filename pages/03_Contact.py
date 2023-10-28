from pathlib import Path
import streamlit as st
import pandas as pd

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Jason Yeung"
PAGE_ICON = ":wave:"
NAME = "Jason Yeung"
DESCRIPTION = """
| Project Management |\n
| Corporate Communications |\n
| Computer Programming |\n
"""

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
css_file = current_dir.parent / "styles" / "main.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.title("Contact me")

with st.container():
    contact_form = """
    <form action="https://formsubmit.co/jason.yeungch@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()