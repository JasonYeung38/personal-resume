# 1. pip install streamlit Pillow
# color @ config.toml

import pandas as pd
import streamlit as st
from pathlib import Path
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_jasonyeung.pdf"
profile_pic = current_dir / "assets" / "ProfilePicRound.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Jason Yeung"
PAGE_ICON = ":wave:"
NAME = "Jason Yeung"
DESCRIPTION = """
| Project Management |\n
| Corporate Communications |\n
| Computer Programming |\n
"""
EMAIL = "jason.yeungch@gmail.com"
SOCIAL_MEDIA = {
    "Personality - Logistician (ISTJ-A)": "https://www.16personalities.com/istj-personality",
    "LinkedIn": "https://www.linkedin.com/in/jasonyeungch/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    # read PDF as binary
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION
with st.container():
    st.write("#")
    col1, col2 = st.columns(2, gap="small")
    # column 1: profile picture
    with col1:
        st.image(profile_pic, width=270)
    # column 2: personal info and download resume
    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application-octet-stream",
        )
        st.write(" 📮 ", EMAIL)

# --- SOCIAL LINKS ---
with st.container():
    st.write("#")
    cols = st.columns(len(SOCIAL_MEDIA))
    # iterate over dictionary
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & Education ---
with st.container():
    st.write("#")
    st.subheader("Experience & Education")
    st.write(
        """
    - ✔️ Seasoned Marketing and Corporate Communications Professional
    - ✔️ Project Management Professional (PMP)®
    - 👨🏻‍🎓 B.A. Journalism and Mass Communications
    - 👨🏻‍🎓 Computer Programming Diploma (complete in this Fall)
    """
    )

# --- SKILLS ---
with st.container():
    st.write("#")
    st.subheader("Soft & Hard Skills")
    st.write(
        """
    - 🧑🏻‍💼 Project Management: Communications, Time and Budget Management, Planning and Organising
    - 🧑🏻‍💻 Productivity Apps: Microsoft 365, Google Workplace
    - 💻 Programming & Database: Python, HTML, CSS, JavaScript, C++, C, Oracle SQL Developer
    - 🎥 Video Editing: Adobe Premiere Pro, Final Cut Pro X
    """
    )

# --- WORK HISTORY ---
with st.container():
    st.write("#")
    st.write("---")
    st.subheader("Work History")

# --- JOB 1
with st.container():
    st.write("**Communications Specialist | Vanke**")
    st.write("07/2017 - 04/2022")
    st.write("""
    - ▶ Played a key role in sales, marketing, and media relations at Vanke Hong Kong, successfully establishing the company's presence and reputation in the HK market.
    - ▶ Planned and executed effective sales, marketing and social media campaigns, achieving sales targets and driving customer engagement for residential and serviced apartment product launches.
    - ▶ Demonstrated strong crisis management skills through proactive news monitoring and handling sensitive situations to protect the corporate image.
    - ▶ Conducted in-depth market analysis, providing valuable insights for management decision-making.
    - ▶ Managed media relations, arranging feature interviews and efficiently handling media inquiries, fostering positive relationships and enhancing brand visibility.
    """)

    # --- JOB 2
    st.write("**Assistant Officer | Lai Sun Group**")
    st.write("09/2016 - 07/2017")
    st.write("""
    - ▶ Contributed to the successful launch of the first residential project with over 600 units in Hong Kong by formulating and implementing effective sales and marketing strategies.
    - ▶ Established and maintained strong relationships with business associates, including property agents, solicitors, and advertising agencies, to ensure seamless collaboration and maximize sales opportunities.
    """)

    # --- JOB 3
    st.write("**Journalist & Anchor | Metro Broadcast & DBC Radio**")
    st.write("06/2015 - 08/2017")
    st.write("""
    - ▶ Conducted extensive research and delivered credible news content with a professional and persuasive tone for radio audiences in two different stations.
    - ▶ Covered both local and complex financial news, engaging and informing listeners effectively.
    """)


st.write("#")
st.write("---")
st.markdown(''' <a target="_self" href="#jason-yeung">
                    <button>
                        Back to Top
                    </button>
                </a>''', unsafe_allow_html=True)

