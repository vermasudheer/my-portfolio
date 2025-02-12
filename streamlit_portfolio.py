import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Sudheer Verma - Portfolio", page_icon="🚀", layout="wide")

# Custom CSS for theme and UI enhancements
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

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About Me", "Experience", "Projects", "Skills", "Certifications", "Blog", "Contact"])

# Sidebar - Education Details
st.sidebar.markdown("### 🎓 Education")
st.sidebar.write("**B. Tech - M. Tech (Dual Degree)**")
st.sidebar.write("Indian Institute of Technology (IIT) Kanpur, 2021")

# About Me Section
if page == "About Me":
    st.title("About Me")
    st.write("🌟 Where data meets mathematics, insights bloom, and patterns unfold.")
    st.write("I am a Solution Analyst specializing in **data analytics, visualization, and pipeline development.** Passionate about solving business problems using data-driven approaches.")
    st.write(f"📞 Contact: +91 9019506060")
    st.write(f"🔗 [LinkedIn](https://www.linkedin.com/in/sudheer-verma-293b4416a/)")
    st.write(f"🔗 [GitHub](https://github.com/vermasudheer)")

# Experience Section
elif page == "Experience":
    st.title("Experience")
    
    st.subheader("Solution Analyst - ExxonMobil (Dec 2024 - Present)")
    st.write("""
    - Develop and maintain dashboards for the Procurement department using **Tableau, Power BI, SQL, and Snowflake**.
    - Build customized insights and develop logics for key procurement metrics.
    - Collaborate with **Procurement Teams, Data Engineers, and Management** to deliver analytics solutions.
    - Prepare technical documentation and train end-users on dashboards and reports.
    - Built robust data pipelines in **Snowflake** to automate data flows.
    """)
    
    st.subheader("Data Analyst - Merck Group (May 2023 - Dec 2024)")
    st.write("""
    - Developed batch and real-time data pipelines in **Palantir Foundry**, automating workflows and eliminating **4 FTE hours annually**.
    - Enhanced data processing efficiency using **Python, SQL, and PySpark**.
    - Designed a high-performance, reusable architecture that improved data accessibility and reduced processing times.
    - Improved query speed by 25% through Indexing, Cardinality Analysis, and Apache Spark optimizations.
    - Created interactive dashboards integrating **SQL & Python** for automated updates, increasing efficiency and performance tracking.
    """)

# Projects Section
elif page == "Projects":
    st.title("Projects")
    st.write("🚀 **PO Recycling Prediction Model** - Predicts PO recycling trends to improve procurement efficiency.")
    st.write("📡 **Telecom Data Pipeline** - Built an ETL pipeline for telecom data using **Azure Data Factory, Databricks, and Snowflake**.")
    st.write("📊 **Tender Dashboard** - Developed an interactive procurement dashboard, reducing data lag by 30 days.")

# Skills Section
elif page == "Skills":
    st.title("Skills")
    st.write("### Languages & Frameworks")
    st.write("- Python, SQL, PySpark")
    
    st.write("### Tools & Libraries")
    st.write("- Apache Hadoop, Apache Spark, Power BI, Tableau, Palantir Foundry")
    
    st.write("### Cloud Technologies")
    st.write("- **Azure:** Data Factory, Databricks, Synapse")
    st.write("- **Databases:** Snowflake, ETL Optimization")

# Certifications Section
elif page == "Certifications":
    st.title("Certifications")
    st.write("📜 **Azure Data Engineer Associate** - [View Certificate](#)")
    st.write("📜 **Google Data Analytics Professional** - [View Certificate](#)")
    st.write("📜 **Snowflake Data Warehouse Specialist** - [View Certificate](#)")

# Blog Section
elif page == "Blog":
    st.title("Blog")
    st.write("📝 [Optimizing ETL Pipelines for Large-Scale Data](#)")
    st.write("📝 [The Role of Data Engineering in AI](#)")
    st.write("📝 [Power BI vs Tableau: Which One to Choose?](#)")

# Contact Section
elif page == "Contact":
    st.title("Contact Me")
    st.write(f"📞 Contact: +91 9019506060")
    st.write(f"🔗 [LinkedIn](https://www.linkedin.com/in/sudheer-verma-293b4416a/)")
    st.write(f"🔗 [GitHub](https://github.com/vermasudheer)")
