import streamlit as st
from backend import Job_Scraper
from component import page_style
from PIL import Image
import pandas as pd

page_style()

class Fake_Job_Portal_Scraper_App:
    # Title of the Streamlit app
    st.title("Job Portal Scraper 🪄")

    pic = Image.open("assets/Job_Portal.png")
    st.image(pic, width=500)

    # Link to the job portal
    st.markdown("[Visit the Job Portal](https://realpython.github.io/fake-jobs/)", unsafe_allow_html=True)

    # Initialize jobs_df to an empty DataFrame
    jobs_df = pd.DataFrame()

    # Button to scrape jobs
    if st.button("Scrape Jobs Metrics"):
        # Call the scrape_jobs method from Job_Scraper class
        jobs_df = Job_Scraper.scrape_jobs()

        # Display the results in the Streamlit app
        if not jobs_df.empty:
            st.subheader("Job Metrics Found:")
            st.dataframe(jobs_df)
            st.snow()
        else:
            st.write("No job metrics found.")

if __name__ == "__main__":
    Fake_Job_Portal_Scraper_App()