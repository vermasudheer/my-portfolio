import streamlit as st

# Set page title and layout
st.set_page_config(page_title="My Portfolio", page_icon="🚀", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Experience", "Projects", "Skills", "Education", "About Me", "Contact"])

# Home Page
if page == "Home":
    st.title("Welcome to My Portfolio")
    st.subheader("Solution Analyst | Data Engineer | Data Analyst")
    st.write("I specialize in building scalable data solutions, developing analytics dashboards, and optimizing ETL pipelines.")

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

    st.subheader("Data Analyst - Merck Group (May 2023 - Dec 2024)")
    st.write("""
    - Developed **batch and real-time data pipelines** in **Palantir Foundry**, automating workflows and saving 4 FTE hours annually.
    - Leveraged **Python, SQL, and PySpark** to enhance data processing efficiency.
    - Designed high-performance, reusable architectures for cross-departmental insights.
    - Applied **Normalization, Denormalization, and Dimensional Modeling** to optimize data structures, improving query performance by 30%.
    - Increased query speed by 25% using **Indexing, Cardinality Analysis, and Apache Spark optimizations**.
    - Created interactive dashboards integrating **SQL & Python**, improving workflow efficiency.
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

# About Me Page
elif page == "About Me":
    st.title("About Me")
    st.subheader("Motto")
    st.write("🌟 *Where data meets mathematics, insights bloom, and patterns unfold.*")
    st.write("I'm passionate about solving business challenges using data-driven solutions. I love optimizing data pipelines and uncovering insights through analytics.")

# Contact Page
elif page == "Contact":
    st.title("Contact Me")
    st.write("[LinkedIn](https://linkedin.com/in/your-profile)")
    st.write("[GitHub](https://github.com/your-github)")
