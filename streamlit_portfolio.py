import streamlit as st
from PIL import Image
import requests

# Cache the profile image to avoid multiple requests
@st.cache_data
def load_profile_image(url):
    return Image.open(requests.get(url, stream=True).raw)

# Load Profile Image
profile_image_url = "https://raw.githubusercontent.com/vermasudheer/my-portfolio/main/profile.jpg"
profile_image = load_profile_image(profile_image_url)

# Custom Styles
st.markdown(
    """
    <style>
        .navbar { background-color: #2c3e50; padding: 15px; text-align: left; color: white; font-size: 24px; font-weight: bold; }
        .sidebar .sidebar-content { background-color: #2c3e50; color: white; }
        .stButton button { background-color: #3498db; color: white; }
        .stButton button:hover { background-color: #2980b9; }
        .highlight { font-weight: bold; color: #e74c3c; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Navigation
page = st.sidebar.radio("Navigate", ["About Me", "Experience", "Projects", "Certifications", "Blog", "Contact"])

# About Me Section
if page == "About Me":
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(profile_image, width=200)
    with col2:
        st.title("Sudheer Verma")
        st.write("Experienced Data Engineer specializing in optimizing data pipelines, dashboarding, and cloud-based infrastructures.")
        st.write("📍 Based in India, currently working at ExxonMobil.")
        st.markdown("**Education:** B.Tech - M.Tech (Dual Degree) from IIT Kanpur")

# Experience Section
elif page == "Experience":
    st.header("Professional Experience")
    with st.expander("Solution Analyst | ExxonMobil"):
        st.write("- Develop dashboards for Procurement KPIs using **Tableau, Power BI, SQL, and Snowflake**.")
        st.write("- Build robust **data pipelines** in Snowflake, ensuring clean and efficient data transformation.")
    
    with st.expander("Data Analyst | Merck Group"):
        st.write("- Automated **batch and real-time data pipelines** in Palantir Foundry.")
        st.write("- Optimized data structures and improved query performance.")

# Projects Section
elif page == "Projects":
    st.header("Key Projects")
    projects = {
        "Predicting Purchase Order (PO) Recycling": "https://github.com/vermasudheer/po-recycling",
        "Optimized ETL Pipeline in Snowflake": "https://github.com/vermasudheer/etl-snowflake"
    }
    
    for project, link in projects.items():
        with st.expander(project):
            st.write(f"[GitHub Repository]({link})")

# Certifications Section
elif page == "Certifications":
    st.header("Certifications")
    with st.expander("Azure Fundamentals - Microsoft"):
        st.markdown("[View Certificate](https://www.microsoft.com/en-us/learning/certification-overview.aspx)")
    with st.expander("Snowflake Hands-On Essentials"):
        st.markdown("[View Certificate](https://www.snowflake.com/training/)")
    with st.expander("Power BI Data Analyst"):
        st.markdown("[View Certificate](https://learn.microsoft.com/en-us/certifications/power-bi-data-analyst-associate/)")

# Blog Section
elif page == "Blog":
    st.header("Blog Posts")
    st.write("Coming soon! 🚀 Stay tuned for insights on **data engineering, cloud analytics, and procurement tech trends**.")

# Contact Section
elif page == "Contact":
    st.header("Get in Touch")
    st.write("📧 Email: sudheerverma25@gmail.com")
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/sudheer-verma-293b4416a/)")
    st.markdown("🐙 [GitHub](https://github.com/vermasudheer)")
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("Thank you for reaching out! I'll get back to you soon.")
