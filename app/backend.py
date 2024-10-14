import requests
from bs4 import BeautifulSoup
import pandas as pd

class Job_Scraper:
    # URL of job portal
    url = 'https://realpython.github.io/fake-jobs/'

    @classmethod
    def scrape_jobs(cls):
        # Send a request to the job portal
        html = requests.get(cls.url)

        # Parse the HTML content
        s = BeautifulSoup(html.content, 'html.parser')
        results = s.find(id='ResultsContainer')

        # Find all job titles and company names
        job_titles = results.find_all('h2', class_='title is-5')
        company_titles = results.find_all('h3', class_='subtitle is-6 company')
        company_location = results.find_all('p', class_='location')
        date_posted = results.find_all('time')

        # Extract text from each job title and company name
        titles = [job.text for job in job_titles]
        companies = [company.text for company in company_titles]
        companies_loc = [loc.text for loc in company_location]
        dates = [date['datetime'] for date in date_posted]  # Use the 'datetime' attribute

        # Ensure all lists have the same length by finding the minimum length
        min_length = min(len(titles), len(companies), len(companies_loc), len(dates))

        # Slice the lists to the minimum length
        titles = titles[:min_length]
        companies = companies[:min_length]
        companies_loc = companies_loc[:min_length]
        dates = dates[:min_length]

        # Combine the titles and companies into a DataFrame
        jobs_df = pd.DataFrame({
            'Date Posted': dates,
            'Job Titles': titles,
            'Company Names': companies,
            'Company Locations': companies_loc,
        })

        return jobs_df
