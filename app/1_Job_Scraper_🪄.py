import streamlit as st
from backend import Job_Scraper
from component import page_style
from PIL import Image

page_style()

# Title of the Streamlit app
st.title("Job Portal Scraper 🪄")

pic = Image.open("assets/Job_Portal.png")
st.image(pic, use_column_width=True)

# Button to scrape jobs
if st.button("Scrape Jobs"):
    # Call the scrape_jobs method from Job_Scraper class
    job_titles = Job_Scraper.scrape_jobs()
    
    # Display the results in the Streamlit app
    if job_titles:
        st.subheader("Job Titles Found:")
        for title in job_titles:
            st.write(title)
    else:
        st.write("No job titles found.")
