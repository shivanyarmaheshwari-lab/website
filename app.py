import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Shivanya Maheshwari", layout="wide")

html_path = Path(__file__).parent / "index.html"

html = html_path.read_text(encoding="utf-8")

components.html(html, height=1400, scrolling=True)
