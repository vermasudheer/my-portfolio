import streamlit as st
from PIL import Image
import requests

# Load Profile Image from GitHub Repo
profile_image_url = "https://raw.githubusercontent.com/vermasudheer/my-portfolio/main/assets/profile.jpg"
profile_image = Image.open(requests.get(profile_image_url, stream=True).raw)

# Custom Styles
st.markdown(
    """
    <style>
        .navbar { background-color: #2c3e50; padding: 15px; text-align: center; color: white; font-size: 24px; font-weight: bold; }
        .sidebar .sidebar-content { background-color: #2c3e50; color: white; }
        .stButton button { background-color: #3498db; color: white; }
        .stButton button:hover { background-color: #2980b9; }
        .highlight { font-weight: bold; color: #e74c3c; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About Me", "Experience", "Projects", "Certifications", "Blog", "Contact"])

# About Me Section
if page == "About Me":
    st.image(profile_image, width=200)
    st.title("Sudheer Verma")
    st.write("Solution Analyst | Data Engineer | Procurement Analytics | Cloud Technologies")
    st.write("With over 3 years of experience in data engineering and analytics, I specialize in optimizing data pipelines, enhancing dashboarding solutions, and leveraging cloud-based infrastructures for large-scale data management.")
    st.write("📍 Based in India, currently working at ExxonMobil.")
    st.markdown("**Education:** B.Tech - M.Tech (Dual Degree) from IIT Kanpur")

# Experience Section
elif page == "Experience":
    st.header("Professional Experience")
    st.subheader("Solution Analyst | ExxonMobil")
    st.write("- Develop, maintain, and enhance dashboards for Procurement KPIs using **Tableau, Power BI, SQL, and Snowflake**.")
    st.write("- Build robust **data pipelines** in Snowflake, ensuring clean and efficient data transformation.")
    st.write("- Collaborate with cross-functional teams to enhance procurement analytics.")
    
    st.subheader("Data Analyst | Merck Group")
    st.write("- Automated **batch and real-time data pipelines** in Palantir Foundry, saving 4 FTE hours annually.")
    st.write("- Optimized data structures with **normalization, denormalization, and dimensional modeling** for improved query performance.")
    st.write("- Developed interactive dashboards to visualize operational metrics, increasing workflow efficiency.")

# Projects Section
elif page == "Projects":
    st.header("Key Projects")
    st.write("🚀 **Predicting Purchase Order (PO) Recycling**")
    st.write("- Designed a machine learning model to predict PO recycling trends, reducing inefficiencies in procurement workflows.")
    st.write("- Integrated insights into Tableau dashboards for real-time monitoring.")
    
    st.write("📊 **Optimized ETL Pipeline in Snowflake**")
    st.write("- Built and optimized ETL pipelines for procurement data, ensuring data governance and compliance.")
    st.write("- Implemented indexing and partitioning, reducing query times by 30%.")

# Certifications Section
elif page == "Certifications":
    st.header("Certifications")
    st.markdown("✅ [Azure Fundamentals - Microsoft](https://www.microsoft.com/en-us/learning/certification-overview.aspx)")
    st.markdown("✅ [Snowflake Hands-On Essentials](https://www.snowflake.com/training/)")
    st.markdown("✅ [Power BI Data Analyst](https://learn.microsoft.com/en-us/certifications/power-bi-data-analyst-associate/)")

# Blog Section
elif page == "Blog":
    st.header("Blog Posts")
    st.write("Coming soon! 🚀 Stay tuned for insights on **data engineering, cloud analytics, and procurement tech trends**.")

# Contact Section
elif page == "Contact":
    st.header("Get in Touch")
    st.write("📧 Email: sudheer@example.com")
    st.markdown("🔗 LinkedIn: [Sudheer Verma](https://www.linkedin.com/in/sudheer-verma-293b4416a/)")
    st.markdown("🐙 GitHub: [vermasudheer](https://github.com/vermasudheer)")
