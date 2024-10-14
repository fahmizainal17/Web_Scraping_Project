import requests
from bs4 import BeautifulSoup
import pandas as pd

class Job_Scraper:
    # URL of job portal
    url = 'https://realpython.github.io/fake-jobs/'

    @classmethod
    def scrape_jobs(cls):
        html =requests.get(cls.url)

        s = BeautifulSoup(html.content, 'html.parser')

        results = s.find(id='ResultsContainer')

        job_titles = results.find_all('h2', class_='title is-5')

        company_titles = results.find_all('h3', class_='subtitle is-6 company')

        # Extract text from each job title and company name
        titles = [job.text for job in job_titles]
        companies = [company.text for company in company_titles]

        # Create a DataFrame with both job titles and company names
        jobs_df = pd.DataFrame({
            "Job Titles": titles,
            "Company Names": companies
        })

        return jobs_df