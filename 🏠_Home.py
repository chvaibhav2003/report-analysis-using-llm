import streamlit as st  
from src.pipeline import Pipeline
from dotenv import load_dotenv
import os

# Load environment variables
check = load_dotenv()

# Set page configuration
st.set_page_config(page_title="🩺 Medical Report Analyzer", page_icon="*")

# Add a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Medical Report Analyzer", "About Me"])

# Medical Report Analyzer Page
if page == "Medical Report Analyzer":
    st.markdown("<h1 style='text-align: center;'>Medical Report Analyzer 🔎</h1>", unsafe_allow_html=True)
    st.caption("Health Insights Based on The Lab Reports")

    # API key input
    if not check:
        api_key = st.text_input("API KEY", placeholder='Provide google api key', help="click to get api key : https://ai.google.dev/")
        os.environ['GOOGLE_API_KEY'] = api_key

    # File uploader for lab reports
    file = st.file_uploader(label="Upload Lab Report", type=["PDF", "JPG", "PNG", "JPEG"])

    # Button to process the report
    if st.button("Process"):
        if file is not None:
            file_type = file.name.split(".")[-1]
            response = Pipeline.process(file=file, type=file_type)
            st.write(response)  # Display the processed response

        else:
            st.warning("Please Upload file.", icon="⚠️")

# About Me Page
elif page == "About Me":
    st.markdown("<h1 style='text-align: center;'>About Me 🧑‍💻</h1>", unsafe_allow_html=True)
    
    # Add information about the developer
    st.write("### Developer Profile")
    st.write("""
    **Name**: Your Name  
    **Role**: Developer & AI Enthusiast  
    **Skills**:  
    - Machine Learning  
    - Natural Language Processing  
    - Full-Stack Development  
    - Cloud Computing  

    **About Me**:  
    I'm a passionate developer with experience in AI and machine learning. This project is aimed at simplifying the process of understanding medical reports using cutting-edge language models and AI technology.  
    """)
    
    # Add any other information like social media links, GitHub, or portfolio
    st.write("### Find me on:")
    st.markdown("""
    - [GitHub](https://github.com/your-username)  
    - [LinkedIn](https://linkedin.com/in/your-profile)  
    """)

