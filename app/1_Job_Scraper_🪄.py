import streamlit as st
from backend import Job_Scraper
from component import page_style
from PIL import Image
import pandas as pd

page_style()

# Title of the Streamlit app
st.title("Job Portal Scraper 🪄")

pic = Image.open("assets/Job_Portal.png")
st.image(pic, width=500)

# Button to scrape jobs
if st.button("Scrape Jobs Metrics"):
    # Call the scrape_jobs method from Job_Scraper class
    job_titles = Job_Scraper.scrape_jobs()
    
    # Display the results in the Streamlit app
    if not jobs_df.empty:
        st.subheader("Job Metrics Found:")
        st.dataframe(jobs_df)
    else:
        st.write("No job metrics found.")
