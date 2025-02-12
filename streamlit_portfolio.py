import streamlit as st

# Set page title and layout
st.set_page_config(page_title="My Portfolio", page_icon="🚀", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Blog", "Contact"])

# Home Page
if page == "Home":
    st.title("Welcome to My Portfolio")
    st.subheader("Data Engineer | Data Scientist | Consultant")
    st.write("I design scalable data solutions and optimize ETL processes. Explore my work!")

# Projects Page
elif page == "Projects":
    st.title("Projects")
    st.write("1. **PO Recycling Prediction Model**")
    st.write("2. **Telecom Data Pipeline**")
    st.write("3. **Tender Dashboard**")

# Blog Page
elif page == "Blog":
    st.title("Blog")
    st.write("Coming Soon!")

# Contact Page
elif page == "Contact":
    st.title("Contact Me")
    st.write("[LinkedIn](https://linkedin.com/in/your-profile)")
    st.write("[GitHub](https://github.com/your-github)")
