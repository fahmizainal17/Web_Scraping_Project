import requests
from bs4 import BeautifulSoup
import pandas as pd

class Job_Scraper:
    # URL of the IMDb Top 250 Movies page
    url = 'https://realpython.github.io/fake-jobs/'

    html =requests.get(url)

    s = BeautifulSoup(html.content, 'html.parser')

    results = s.find(id='ResultsContainer')

    job_title = results.find_all('h2', class_='title is-5')

    for job in job_title:
        print(job.text)
