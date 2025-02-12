import streamlit as st

# Set page title and layout with custom background color
st.set_page_config(page_title="My Portfolio", page_icon="🚀", layout="wide")

# Custom CSS for styling
st.markdown(
    '''
    <style>
        body {
            background-color: #f5f7fa;
        }
        .sidebar .sidebar-content {
            background-color: #1e3a8a; /* Dark Blue */
        }
        .stButton>button {
            background-color: #4f46e5;
            color: white;
            font-weight: bold;
        }
        .stRadio > div {
            background-color: white;
            padding: 10px;
            border-radius: 10px;
        }
        .main-content {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
    </style>
    ''',
    unsafe_allow_html=True
)

# Sidebar navigation with improved styling
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About Me", "Experience", "Projects", "Skills", "Education", "Certifications", "Blog", "Contact"])

# About Me Section (First Section)
if page == "About Me":
    st.title("About Me")
    st.write("🌟 Where data meets mathematics, insights bloom, and patterns unfold.")
    st.write("I am a Solution Analyst specializing in **data analytics, visualization, and pipeline development.** Passionate about solving business problems using data-driven approaches.")
    st.write("[LinkedIn](https://linkedin.com/in/your-profile) | [GitHub](https://github.com/your-github)")

# Experience Page
elif page == "Experience":
    st.title("Experience")

    st.subheader("Solution Analyst - ExxonMobil (Dec 2024 - Present)")
    st.write("""
    - Develop, maintain, and enhance dashboards and visualizations for the Procurement department using **Tableau, Power BI, SQL, and Snowflake**.
    - Develop logics & calculations for metrics, build customized insights to support procurement stakeholders globally.
    - Collaborate with **Procurement Teams, Data Engineers, and Management** to deliver analytics solutions.
    - Troubleshoot issues related to data and dashboards, ensuring smooth reporting.
    - Prepare technical documentation and train end-users on dashboards and reports.
    - Built robust data pipelines in **Snowflake** to automate data flows.
    """)

# Projects Page
elif page == "Projects":
    st.title("Projects")
    st.write("🚀 **PO Recycling Prediction Model** - Predicts PO recycling trends to improve procurement efficiency.")
    st.write("📡 **Telecom Data Pipeline** - Built an end-to-end ETL pipeline for telecom data using **Azure Data Factory, Databricks, and Snowflake**.")
    st.write("📊 **Tender Dashboard** - Developed an interactive procurement dashboard, reducing data lag by 30 days.")

# Skills Page
elif page == "Skills":
    st.title("Skills")
    st.write("### Languages & Frameworks")
    st.write("- Python, SQL, PySpark")
    
    st.write("### Tools & Libraries")
    st.write("- Apache Hadoop, Apache Spark, Power BI, Tableau, Palantir Foundry")
    
    st.write("### Cloud Technologies")
    st.write("- **Azure:** Data Factory, Databricks, Synapse")
    st.write("- **Databases:** Snowflake, ETL Optimization")

# Education Page
elif page == "Education":
    st.title("Education")
    st.subheader("B. Tech - M. Tech (Dual Degree)")
    st.write("**Indian Institute of Technology (IIT) Kanpur - 2021**")

# Certifications Page
elif page == "Certifications":
    st.title("Certifications")
    st.write("📜 **Azure Data Engineer Associate** - [View Certificate](#)")
    st.write("📜 **Google Data Analytics Professional** - [View Certificate](#)")
    st.write("📜 **Snowflake Data Warehouse Specialist** - [View Certificate](#)")

# Blog Page
elif page == "Blog":
    st.title("Blog")
    st.write("📝 [Optimizing ETL Pipelines for Large-Scale Data](#)")
    st.write("📝 [The Role of Data Engineering in AI](#)")
    st.write("📝 [Power BI vs Tableau: Which One to Choose?](#)")

# Contact Page
elif page == "Contact":
    st.title("Contact Me")
    st.write("[LinkedIn](https://linkedin.com/in/your-profile)")
    st.write("[GitHub](https://github.com/your-github)")
