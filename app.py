from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Shivanya Maheshwari",
    page_icon="🌸",
    layout="wide",
)


html_path = Path(__file__).resolve().parent / "index.html"
html = html_path.read_text(encoding="utf-8")

components.html(html, height=1600, scrolling=True)
