import streamlit as st
from PIL import Image
import requests
import io
import re

# Cache the profile image to avoid multiple requests
@st.cache_data
def load_profile_image(url):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        return Image.open(io.BytesIO(response.content))
    except requests.exceptions.RequestException:
        return None

# Load Profile Image
profile_image_url = "https://raw.githubusercontent.com/vermasudheer/my-portfolio/main/profile.jpg"
profile_image = load_profile_image(profile_image_url)

# Apply Custom Styles
def apply_custom_styles():
    st.markdown(
        """
        <style>
            .navbar { background-color: #2c3e50; padding: 15px; text-align: left; color: white; font-size: 24px; font-weight: bold; }
            .sidebar .sidebar-content { background-color: #2c3e50; color: white; }
            .stButton button { background-color: #3498db; color: white; }
            .stButton button:hover { background-color: #2980b9; }
            .highlight { font-weight: bold; color: #e74c3c; }
            .main-container { background-color: #f7f9fc; padding: 20px; border-radius: 10px; }
        </style>
        """,
        unsafe_allow_html=True,
    )

apply_custom_styles()

# Define Page Sections
def show_about():
    col1, col2 = st.columns([1, 2])
    with col1:
        if profile_image:
            st.image(profile_image, width=200)
        else:
            st.warning("Profile image could not be loaded.")
    with col2:
        st.title("Sudheer Verma")
        st.write("Experienced Data Engineer specializing in optimizing data pipelines, dashboarding, and cloud-based infrastructures.")
        st.write("📍 Based in India, currently working at ExxonMobil.")
        st.markdown("**Education:** B.Tech - M.Tech (Dual Degree) from IIT Kanpur")

def show_experience():
    st.header("Professional Experience")

    with st.expander("Solution Analyst | ExxonMobil (Dec 2024 - Present)"):
        st.markdown("""
        - Develop dashboards for Procurement KPIs using **Tableau, Power BI, SQL, and Snowflake**.
        - Build robust **data pipelines** in Snowflake, ensuring clean and efficient data transformation.
        """)

    with st.expander("Data Analyst | Merck Group (May 2023 - Dec 2024)"):
        st.markdown("""
        - Automated **batch and real-time data pipelines** in Palantir Foundry.
        - Optimized data structures and improved query performance.
        """)

def show_projects():
    st.header("Key Projects")

    projects = [
        {
            "title": "Predicting Purchase Order (PO) Recycling",
            "description": "Developed a machine learning model to predict purchase order recycling patterns, reducing manual interventions and optimizing procurement workflows.",
            "link": "https://github.com/vermasudheer/po-recycling"
        },
        {
            "title": "Optimized ETL Pipeline in Snowflake",
            "description": "Designed and implemented an efficient ETL pipeline using Snowflake and SQL, reducing data processing time by 40%.",
            "link": "https://github.com/vermasudheer/etl-snowflake"
        }
    ]
    
    for project in projects:
        st.markdown(f"""
        <div style="border: 1px solid #ccc; padding: 15px; border-radius: 8px; margin-bottom: 10px; background-color: #f9f9f9;">
            <h4>{project['title']}</h4>
            <p>{project['description']}</p>
            🔗 <a href="{project['link']}" target="_blank"><b>GitHub Repository</b></a>
        </div>
        """, unsafe_allow_html=True)

def show_certifications():
    st.header("Certifications")

    certifications = {
        "Azure Fundamentals - Microsoft": "https://www.microsoft.com/en-us/learning/certification-overview.aspx",
        "Snowflake Hands-On Essentials": "https://www.snowflake.com/training/",
        "Power BI Data Analyst": "https://learn.microsoft.com/en-us/certifications/power-bi-data-analyst-associate/"
    }
    
    for cert, link in certifications.items():
        st.markdown(f"✔ **{cert}:** [Certificate Link]({link})")

def show_blog():
    st.header("Blog Posts")

    blogs = [
        {"title": "Data Engineering Best Practices", "link": "#"},
        {"title": "Cloud Analytics Optimization Techniques", "link": "#"},
        {"title": "Procurement Tech Trends and Analysis", "link": "#"}
    ]

    for blog in blogs:
        st.markdown(f"📌 **{blog['title']}:** [Read More]({blog['link']})")

def show_contact():
    st.sidebar.header("Get in Touch")
    st.sidebar.write("📧 Email: sudheerverma25@gmail.com")
    st.sidebar.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/sudheer-verma-293b4416a/)")
    st.sidebar.markdown("🐙 [GitHub](https://github.com/vermasudheer)")
    
    st.header("Send a Message")
    with st.form("contact_form"):
        name = st.text_input("Name", placeholder="Enter your name")
        email = st.text_input("Email", placeholder="Enter your email")
        message = st.text_area("Message", placeholder="Type your message here")
        submitted = st.form_submit_button("Send Message")
        
        def is_valid_email(email):
            return re.match(r"[^@]+@[^@]+\.[^@]+", email)

        if submitted:
            if not name or not email or not message:
                st.error("Please fill out all fields before submitting.")
            elif not is_valid_email(email):
                st.error("Invalid email format. Please enter a valid email.")
            else:
                st.toast("✅ Thank you for reaching out! I'll get back to you soon.")

# Navigation
page = st.sidebar.radio("Navigate", ["About Me", "Experience", "Projects", "Certifications", "Blog", "Contact"])

# Page Mapping
pages = {
    "About Me": show_about,
    "Experience": show_experience,
    "Projects": show_projects,
    "Certifications": show_certifications,
    "Blog": show_blog,
    "Contact": show_contact
}

# Execute selected page function
pages[page]()
