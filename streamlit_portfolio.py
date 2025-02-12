import streamlit as st
from PIL import Image
import requests

# Cache the profile image to avoid multiple requests
@st.cache_data
def load_profile_image(url):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        return Image.open(response.raw)
    return None

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
        .main-container { background-color: #f7f9fc; padding: 20px; border-radius: 10px; }
        .stRadio > label { background-color: #dfe6e9; padding: 5px; border-radius: 5px; }
        .experience-title { font-weight: bold; color: #2c3e50; font-size: 18px; }
        .experience-duration { font-weight: bold; color: #3498db; }
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
        if profile_image:
            st.image(profile_image, width=200)
    with col2:
        st.title("Sudheer Verma")
        st.write("Experienced Data Engineer specializing in optimizing data pipelines, dashboarding, and cloud-based infrastructures.")
        st.write("📍 Based in India, currently working at ExxonMobil.")
        st.markdown("**Education:** B.Tech - M.Tech (Dual Degree) from IIT Kanpur")

# Experience Section
elif page == "Experience":
    st.header("Professional Experience")
    with st.expander("**Solution Analyst | ExxonMobil** (Dec 2024 - Present)"):
        st.write("- Develop dashboards for Procurement KPIs using **Tableau, Power BI, SQL, and Snowflake**.")
        st.write("- Build robust **data pipelines** in Snowflake, ensuring clean and efficient data transformation.")
    
    with st.expander("**Data Analyst | Merck Group** (May 2023 - Dec 2024)"):
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
        st.markdown(f"### {project}")
        st.write(f"🔗 [GitHub Repository]({link})")
        st.divider()

# Certifications Section
elif page == "Certifications":
    st.header("Certifications")
    certifications = {
        "Azure Fundamentals - Microsoft": "https://www.microsoft.com/en-us/learning/certification-overview.aspx",
        "Snowflake Hands-On Essentials": "https://www.snowflake.com/training/",
        "Power BI Data Analyst": "https://learn.microsoft.com/en-us/certifications/power-bi-data-analyst-associate/"
    }
    
    for cert, link in certifications.items():
        st.markdown(f"- **[{cert}]({link})**")

# Blog Section
elif page == "Blog":
    st.header("Blog Posts")
    st.write("Coming soon! 🚀 Stay tuned for insights on:")
    st.markdown("- Data Engineering best practices")
    st.markdown("- Cloud analytics optimization techniques")
    st.markdown("- Procurement tech trends and analysis")

# Contact Section
elif page == "Contact":
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
        
        if submitted:
            if name and email and message:
                st.success("Thank you for reaching out! I'll get back to you soon.")
            else:
                st.error("Please fill out all fields before submitting.")
