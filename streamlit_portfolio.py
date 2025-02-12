import streamlit as st
from PIL import Image
import requests
import re
import random

# Cache the profile image
@st.cache_data
def load_profile_image(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        return Image.open(response.raw)
    return None

# Load Profile Image
profile_image_url = "https://raw.githubusercontent.com/vermasudheer/my-portfolio/main/profile.jpg"
profile_image = load_profile_image(profile_image_url)

# --- Color Palettes ---
color_palettes = [
    ["#3498db", "#2980b9", "#f0f0f0", "#fff"],  # Blue palette
    ["#e74c3c", "#c0392b", "#f0f0f0", "#fff"],  # Red palette
    ["#2ecc71", "#27ae60", "#f0f0f0", "#fff"],  # Green palette
    ["#f39c12", "#e67e22", "#f0f0f0", "#fff"],  # Orange palette
    ["#9b59b6", "#8e44ad", "#f0f0f0", "#fff"],  # Purple palette
    ["#1abc9c", "#16a085", "#f0f0f0", "#fff"],  # Teal palette
]

def get_random_palette():
    return random.choice(color_palettes)

# --- Navigation & Color Switching ---
if "current_palette" not in st.session_state:
    st.session_state.current_palette = get_random_palette()

page = st.sidebar.radio("Navigate", ["About Me", "Experience", "Projects", "Certifications", "Blog", "Contact"])

if page != st.session_state.get("current_page", None):
    st.session_state.current_palette = get_random_palette()
    st.session_state["current_page"] = page

current_palette = st.session_state.current_palette
primary_color, secondary_color, background_color, text_color = current_palette

# --- Custom Styles ---
st.markdown(
    f"""
    <style>
    body {{ background-color: {background_color}; }}
    .stButton button {{
        background-color: {primary_color};
        color: {text_color};
        transition: all 0.3s;
    }}
    .stButton button:hover {{
        background-color: {secondary_color};
        transform: scale(1.05);
    }}
    .project-item:hover {{
        transform: scale(1.02);
    }}
    a {{ color: {primary_color} !important; text-decoration: none; }}
    a:hover {{ color: {secondary_color} !important; text-decoration: underline; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- About Me ---
if page == "About Me":
    st.title("Sudheer Verma")
    col1, col2 = st.columns([1, 2])
    with col1:
        if profile_image:
            st.image(profile_image, width=200)
    with col2:
        st.write("Experienced Data Engineer optimizing data pipelines, dashboarding, and cloud-based infrastructures.")
        st.write("📍 Based in India, currently working at ExxonMobil.")
        st.markdown("**Education:** B.Tech - M.Tech (Dual Degree) from IIT Kanpur")

# --- Experience ---
elif page == "Experience":
    st.header("Professional Experience")
    experience_data = [
        {"title": "Solution Analyst | ExxonMobil", "duration": "Dec 2024 - Present", "content": [
            "- Develop dashboards for Procurement KPIs using **Tableau, Power BI, SQL, and Snowflake**.",
            "- Build robust **data pipelines** in Snowflake, ensuring clean and efficient data transformation.",
        ]},
        {"title": "Data Analyst | Merck Group", "duration": "May 2023 - Dec 2024", "content": [
            "- Automated **batch and real-time data pipelines** in Palantir Foundry.",
            "- Optimized data structures and improved query performance.",
        ]},
    ]
    for exp in experience_data:
        with st.expander(f"**{exp['title']}** ({exp['duration']})"):
            for item in exp['content']:
                st.write(item)

# --- Projects ---
elif page == "Projects":
    st.header("Key Projects")
    projects = {
        "Predicting Purchase Order (PO) Recycling": "https://github.com/vermasudheer/po-recycling",
        "Optimized ETL Pipeline in Snowflake": "https://github.com/vermasudheer/etl-snowflake"
    }
    for project, link in projects.items():
        st.markdown(f"[**{project}**]({link})", unsafe_allow_html=True)

# --- Certifications ---
elif page == "Certifications":
    st.header("Certifications")
    certifications = [
        "Microsoft Certified: Azure Data Engineer Associate",
        "Google Data Analytics Professional Certificate",
        "AWS Certified Data Analytics – Specialty"
    ]
    for cert in certifications:
        st.write(f"- {cert}")

# --- Blog ---
elif page == "Blog":
    st.header("Blog Posts")
    st.write("Coming Soon...")

# --- Contact ---
elif page == "Contact":
    st.header("Get in Touch")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send Message")
    if submitted:
        st.success("Thank you! I'll get back to you soon.")
