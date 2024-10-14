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

        # Extract text from each job title
        titles = [job.text for job in job_titles]
        return titles
