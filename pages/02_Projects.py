from pathlib import Path
import streamlit as st
import pandas as pd
# from st_aggrid import AgGrid

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

st.title("Projects")

with st.container():
    st.write("#")
    st.write("---") 
    st.header("Real Estate Projects")
    st.write("- ▶ Planning and executing marketing campaigns for real estate development projects")
    # load data
    @st.cache_data
    def data_upload():
        df = pd.read_csv("ResProjects.csv")
        return df
    df = data_upload()
    st.dataframe(data=df, hide_index=True)
    # st.info(len(df))
