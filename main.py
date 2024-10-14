import streamlit as st
from backend import JobScraper

# Title of the Streamlit app
st.title("Job Scraper")

# Button to scrape jobs
if st.button("Scrape Jobs"):
    # Call the scrape_jobs method from JobScraper class
    job_titles = JobScraper.scrape_jobs()
    
    # Display the results in the Streamlit app
    if job_titles:
        st.subheader("Job Titles Found:")
        for title in job_titles:
            st.write(title)
    else:
        st.write("No job titles found.")
