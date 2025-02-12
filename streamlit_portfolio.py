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
        .navbar {
            padding: 10px;
            color: white;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
        }
    </style>
    ''',
    unsafe_allow_html=True
)

# Sidebar navigation
page = st.sidebar.radio("", ["About Me", "Experience", "Projects", "Certifications", "Blog", "Contact"], index=0)

# Sidebar - Education Details
st.sidebar.markdown("### 🎓 Education")
st.sidebar.write("**B. Tech - M. Tech (Dual Degree)**")
st.sidebar.write("Indian Institute of Technology (IIT) Kanpur, 2021")

# About Me & Experience Sections
if page in ["About Me", "Experience"]:
    st.markdown(
        f'<div class="navbar" style="background-image: url(\'https://www.freepik.com/premium-ai-image/business-data-analysis-analytics-customers-insights-with-charts-abstract-blue-background-vector-illustration-generative-ai_38344146.htm\');">{page}</div>',

        unsafe_allow_html=True
    )
    st.image("https://media.licdn.com/dms/image/D4D03AQEbcj1Mnl2DRA/profile-displayphoto-shrink_800_800/0/1701123456789?e=1710009600&v=beta&t=abc123xyz", width=150)
    if page == "About Me":
        st.write("I am a Solution Analyst specializing in **data analytics, visualization, and pipeline development.** Passionate about solving business problems using data-driven approaches.")
    elif page == "Experience":
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
    st.markdown('<div class="navbar" style="background-color: #ff4dff;">Projects</div>', unsafe_allow_html=True)
    st.write("🚀 **PO Recycling Prediction Model** - Predicts PO recycling trends to improve procurement efficiency.")
    st.write("📡 **Telecom Data Pipeline** - Built an ETL pipeline for telecom data using **Azure Data Factory, Databricks, and Snowflake**.")
    st.write("📊 **Tender Dashboard** - Developed an interactive procurement dashboard, reducing data lag by 30 days.")

# Certifications Section
elif page == "Certifications":
    st.markdown('<div class="navbar" style="background-color: #4dffb8;">Certifications</div>', unsafe_allow_html=True)
    st.write("📜 **Azure Data Engineer Associate** - [View Certificate](#)")
    st.write("📜 **Google Data Analytics Professional** - [View Certificate](#)")
    st.write("📜 **Snowflake Data Warehouse Specialist** - [View Certificate](#)")

# Blog Section
elif page == "Blog":
    st.markdown('<div class="navbar" style="background-color: #4dffb8;">Blog</div>', unsafe_allow_html=True)
    st.write("📝 [Optimizing ETL Pipelines for Large-Scale Data](#)")
    st.write("📝 [The Role of Data Engineering in AI](#)")
    st.write("📝 [Power BI vs Tableau: Which One to Choose?](#)")

# Contact Section
elif page == "Contact":
    st.markdown('<div class="navbar" style="background-color: #4ddbff;">Contact Me</div>', unsafe_allow_html=True)
    st.write(f"🔗 [LinkedIn](https://www.linkedin.com/in/sudheer-verma-293b4416a/)")
    st.write(f"🔗 [GitHub](https://github.com/vermasudheer)")
