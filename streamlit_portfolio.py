import streamlit as st
from PIL import Image
import requests
import io
import re

# Cache the profile image to avoid multiple requests
@st.cache_data
def load_profile_image(url):
    response = requests.get(url, stream=True)
    return Image.open(io.BytesIO(response.content))

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
            .experience-title { font-weight: bold; color: #2c3e50; font-size: 18px; }
            .experience-duration { font-weight: bold; color: #3498db; }
        </style>
        """,
        unsafe_allow_html=True,
    )

apply_custom_styles()

# Define Page Sections
def show_about():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(profile_image, width=200)
    with col2:
        st.title("Sudheer Verma")
        st.write("Experienced Data Engineer specializing in optimizing data pipelines, dashboarding, and cloud-based infrastructures.")
        st.write("📍 Based in India, currently working at ExxonMobil.")
        st.markdown("**Education:** B.Tech - M.Tech (Dual Degree) from IIT Kanpur")

def show_experience():
    st.header("Professional Experience")
    with st.expander("**Solution Analyst | <span style='color:#3498db;'>ExxonMobil</span>** <span class='experience-duration'>(Dec 2024 - Present)</span>", unsafe_allow_html=True):
        st.write("- Develop dashboards for Procurement KPIs using **Tableau, Power BI, SQL, and Snowflake**.")
        st.write("- Build robust **data pipelines** in Snowflake, ensuring clean and efficient data transformation.")
    
    with st.expander("**Data Analyst | <span style='color:#3498db;'>Merck Group</span>** <span class='experience-duration'>(May 2023 - Dec 2024)</span>", unsafe_allow_html=True):
        st.write("- Automated **batch and real-time data pipelines** in Palantir Foundry.")
        st.write("- Optimized data structures and improved query performance.")

def show_projects():
    st.header("Key Projects")
    projects = {
        "Predicting Purchase Order (PO) Recycling": "https://github.com/vermasudheer/po-recycling",
        "Optimized ETL Pipeline in Snowflake": "https://github.com/vermasudheer/etl-snowflake"
    }
    
    for project, link in projects.items():
        st.markdown(f"""
        <div style="border: 1px solid #ccc; padding: 10px; border-radius: 8px; margin-bottom: 10px;">
            <h4>{project}</h4>
            <p>🔗 <a href="{link}" target="_blank">GitHub Repository</a></p>
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
        st.markdown(f"- **[{cert}]({link})**")

def show_blog():
    st.header("Blog Posts")
    st.write("Coming soon! 🚀 Stay tuned for insights on:")
    st.markdown("- Data Engineering best practices")
    st.markdown("- Cloud analytics optimization techniques")
    st.markdown("- Procurement tech trends and analysis")

def show_contact():
    st.sidebar.header("Get in Touch")
    st.sidebar.write("📧 Email: sudheerverma25@gmail.com")
    st.sidebar.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/sudheer-verma-293b4416a/)")
    st.sidebar.markdown("🐙 [GitHub](https://github.com/vermasudheer)")
    
    st.header("Send a Message")
    with st.form("contact_form"):
        name = st.text_input("Name", value="", placeholder="Enter your name")
        email = st.text_input("Email", value="", placeholder="Enter your email")
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
                st.success("Thank you for reaching out! I'll get back to you soon.")

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
