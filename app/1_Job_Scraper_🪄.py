import streamlit as st
from backend import Synthetic_Job_Scraper , Adnexio_Job_Scraper , Future_Job_Scraper
from component import page_style
from PIL import Image
import pandas as pd

# Apply custom styles
page_style()

class Sythetic_Job_Portal_Scraper_App:
    def __init__(self):
        # Title of the Streamlit app
        st.title("Synthetic Job Portal Scraper 🪄")

        pic = Image.open("assets/Synthetic_Job_Portal.png")
        st.image(pic, width=500)

        # Link to the job portal
        st.markdown("[Visit the Job Portal](https://realpython.github.io/fake-jobs/)", unsafe_allow_html=True)

        # Initialize jobs_df to an empty DataFrame
        jobs_df = pd.DataFrame()

        # Button to scrape jobs
        if st.button("Scrape Jobs Metrics",key='fake'):
            # Call the scrape_jobs method from Synthetic_Job_Scraper class
            jobs_df = Synthetic_Job_Scraper.scrape_jobs()

            # Display the results in the Streamlit app
            if not jobs_df.empty:
                st.subheader("Job Metrics Found:")
                st.dataframe(jobs_df)
                st.snow()
            else:
                st.write("No job metrics found.")

class Adnexio_Job_Portal_Scraper:
    def __init__(self):
        st.title("Adnexio Job Portal Scraper 🪄")

        pic = Image.open("assets/Adnexio_Job_Portal.png")
        st.image(pic, width=500)

        st.markdown("[Visit the Adnexio Job Portal](https://career.adnexio.jobs/jobs/)", unsafe_allow_html=True)

        jobs_df = pd.DataFrame()

        if st.button("Scrape Jobs Metrics",key='adx'):
            jobs_df = Adnexio_Job_Scraper.scrape_jobs()

            if not jobs_df.empty:
                st.subheader("Job Metrics Found:")
                st.dataframe(jobs_df)
                st.snow()
            else:
                st.write("No job metrics found.")

class Placeholder_for_Future_Projects:
    def __init__(self):
        st.title("Placeholder for Future Projects 🪄")

        pic = Image.open("assets/Future_Projects.png")
        st.image(pic, width=500)

        st.markdown("[Visit the Placeholder for Future Projects](https://shopee.com.my/)", unsafe_allow_html=True)

        jobs_df = pd.DataFrame()

        if st.button("Scrape Jobs Metrics",key='future'):
            jobs_df = Future_Job_Scraper.scrape_jobs()

            if not jobs_df.empty:
                st.subheader("Job Metrics Found:")
                st.dataframe(jobs_df)
                st.snow()
            else:
                st.write("No job metrics found.")

tab1, tab2, tab3 = st.tabs(["Synthetic_Job_Portal_Scraper", "Adnexio_Job_Portal_Scraper", "Placeholder_for_Future_Projects"])

with tab1:
    Sythetic_Job_Portal_Scraper_App()
with tab2:
    Adnexio_Job_Portal_Scraper()
with tab3:
    Placeholder_for_Future_Projects()