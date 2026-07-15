from pathlib import Path
import base64

import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
LOGO_PATH = BASE_DIR / "skinsense_logo.png"


st.set_page_config(
    page_title="Shivanya Maheshwari | Portfolio",
    page_icon="S",
    layout="centered",
)


st.markdown(
    """
    <style>
      :root {
        --navy: #17345c;
        --blue: #2e7fbe;
        --ink: #26384f;
        --muted: #66778d;
        --line: #dbe8f2;
        --soft-blue: #f1f9ff;
        --soft-pink: #fff3f7;
        --pink: #f3b8c7;
        --white: #ffffff;
      }

      .stApp {
        background: linear-gradient(180deg, #fff8fb 0%, #f3fbff 45%, #ffffff 100%);
        color: var(--ink);
      }

      .block-container {
        max-width: 1040px;
        padding-top: 3.2rem;
        padding-bottom: 4rem;
      }

      h1, h2, h3, p, li, label, span {
        font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }

      h1 {
        color: var(--navy);
        font-size: clamp(3rem, 7vw, 5.4rem) !important;
        line-height: 0.98 !important;
        letter-spacing: -0.035em;
        margin-bottom: 0.5rem;
      }

      h2 {
        color: var(--navy);
        letter-spacing: -0.025em;
      }

      h3 {
        color: var(--navy);
      }

      .eyebrow {
        color: var(--blue);
        font-size: 0.82rem;
        font-weight: 850;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 0.9rem;
      }

      .subtitle {
        color: var(--blue);
        font-size: clamp(1.2rem, 2.4vw, 1.65rem);
        font-weight: 850;
        line-height: 1.3;
        margin: 1rem 0 1rem;
      }

      .body-copy {
        color: var(--muted);
        font-size: 1.06rem;
        line-height: 1.7;
      }

      .card {
        border: 1px solid var(--line);
        border-radius: 24px;
        background: rgba(255, 255, 255, 0.9);
        box-shadow: 0 18px 42px rgba(23, 52, 92, 0.08);
        padding: 1.6rem;
      }

      .highlight-card {
        border-left: 4px solid var(--pink);
        background: linear-gradient(135deg, var(--soft-blue), var(--soft-pink));
      }

      .facts-row {
        display: flex;
        justify-content: space-between;
        gap: 1rem;
        border-top: 1px solid var(--line);
        padding: 0.85rem 0;
        color: var(--muted);
      }

      .facts-row strong {
        color: var(--navy);
      }

      .project-card {
        text-align: center;
        background: linear-gradient(145deg, #ffffff 0%, var(--soft-pink) 42%, var(--soft-blue) 100%);
      }

      .logo-fallback {
        color: var(--navy);
        font-size: 2.6rem;
        font-weight: 950;
        letter-spacing: -0.04em;
        margin-bottom: 0.4rem;
      }

      .section-rule {
        width: 58px;
        height: 4px;
        border-radius: 999px;
        background: var(--pink);
        margin: -0.7rem 0 1.8rem;
      }

      .contact-box {
        border-radius: 24px;
        background: var(--navy);
        color: white;
        padding: 1.6rem;
      }

      .contact-box h2 {
        color: white;
        margin-bottom: 0.2rem;
      }

      .contact-box p {
        color: #dce9f5;
      }

      .stButton > button,
      .stLinkButton > a {
        border-radius: 999px !important;
        min-height: 48px;
        font-weight: 850 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)


def facts_card() -> None:
    st.markdown(
        """
        <div class="card">
          <h2 style="font-size:1.35rem;margin-bottom:1rem;">Quick Facts</h2>
          <div class="facts-row"><strong>School</strong><span>Cathedral and John Connon School</span></div>
          <div class="facts-row"><strong>Grade</strong><span>9</span></div>
          <div class="facts-row"><strong>Age</strong><span>14</span></div>
          <div class="facts-row"><strong>City</strong><span>Mumbai</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_title(title: str) -> None:
    st.markdown(f"## {title}")
    st.markdown('<div class="section-rule"></div>', unsafe_allow_html=True)


def logo_data_uri():
    if not LOGO_PATH.exists():
        return None
    encoded = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def logo_block() -> None:
    logo = logo_data_uri()
    logo_html = (
        f'<img src="{logo}" alt="SkinSense logo" style="width:170px;max-width:72%;height:auto;margin:0 auto 1rem;display:block;" />'
        if logo
        else '<div class="logo-fallback">SkinSense</div>'
    )
    st.markdown(
        f"""
        <div class="card project-card">
          {logo_html}
          <h2 style="margin-top:0.4rem;margin-bottom:0.3rem;">SkinSense</h2>
          <p class="body-copy" style="margin-bottom:0;">
            AI screening support • public health awareness • accessible design
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


left, right = st.columns([1.35, 0.8], gap="large")

with left:
    st.markdown('<div class="eyebrow">Grade 9 • Mumbai • Student Portfolio</div>', unsafe_allow_html=True)
    st.markdown("# Shivanya Maheshwari")
    st.markdown(
        '<p class="subtitle">Curious student, confident speaker, athlete, and young innovator.</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <p class="body-copy">
          I am a 14-year-old Grade 9 student at Cathedral and John Connon School in Mumbai.
          My work brings together communication, leadership, sport, and technology, with a growing interest
          in building thoughtful projects that are practical, useful, and socially aware.
        </p>
        """,
        unsafe_allow_html=True,
    )
    c1, c2 = st.columns(2)
    with c1:
        st.link_button("View My Project", "#project", use_container_width=True)
    with c2:
        st.link_button("Get In Touch", "mailto:shivanya.r.maheshwari@gmail.com", use_container_width=True)

with right:
    facts_card()

st.write("")
st.write("")

section_title("About")
about_left, about_right = st.columns(2, gap="large")

with about_left:
    st.markdown(
        """
        <div class="card">
          <h3>Who I Am</h3>
          <p class="body-copy">
            I am an energetic and ambitious student who enjoys taking on challenges both inside and outside the classroom.
            Debate, MUNs, swimming, and throwball have helped me become more confident, disciplined, and comfortable
            thinking on my feet.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with about_right:
    st.markdown(
        """
        <div class="card highlight-card">
          <h3>What Drives Me</h3>
          <p class="body-copy">
            I am drawn to ideas that combine communication, problem-solving, and real-world impact.
            I enjoy projects that make complex things easier to understand and use, especially when technology
            can support communities in a direct way.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")
st.write("")

st.markdown('<div id="project"></div>', unsafe_allow_html=True)
section_title("Project Spotlight")
project_left, project_right = st.columns([1.15, 0.85], gap="large")

with project_left:
    st.markdown(
        """
        <div class="card">
          <h3>SkinSense</h3>
          <p class="body-copy">
            SkinSense is an AI-powered skin screening concept designed to support Koli fisherwomen and fishermen
            who are regularly exposed to seawater, sun, humidity, and wet work. The project explores how a simple
            app can help users upload or take a photo, answer basic follow-up questions, receive a screening summary,
            and understand when to seek dermatological care.
          </p>
          <p class="body-copy">
            The goal is not to replace doctors, but to make early awareness, health guidance, and access to care easier,
            especially for communities that may face barriers to specialist support.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with project_right:
    logo_block()

st.write("")
st.write("")

st.markdown(
    """
    <div class="contact-box">
      <h2>Contact</h2>
      <p>For project inquiries, school opportunities, or collaboration.</p>
      <p style="margin:0;font-weight:800;">shivanya.r.maheshwari@gmail.com</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("© 2026 Shivanya Maheshwari. Built as a personal academic portfolio.")
