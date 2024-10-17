import requests
from bs4 import BeautifulSoup
import pandas as pd

class Synthetic_Job_Scraper:
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

class Adnexio_Job_Scraper:
    # URL of the job portal
    url = 'https://career.adnexio.jobs/jobs/'

    @classmethod
    def scrape_jobs(cls):
        # Send a request to the job portal
        html = requests.get(cls.url)

        # Parse the HTML content
        s = BeautifulSoup(html.content, 'html.parser')

        # Find all job containers using a general tag (e.g., div) and relevant attributes
        results = s.find_all('div', class_='border-xl relative mx-auto mb-4 grid w-full cursor-pointer grid-cols-12 rounded-xl bg-adx-white py-6')

        if not results:
            print("No job listings found with the specified class. Please verify the class name and structure.")
            return pd.DataFrame()  # Return an empty DataFrame if no results are found

        # Prepare lists to store the scraped data
        titles = []
        companies = []
        locations = []
        salaries = []

        # Iterate through each job container
        for job in results:
            # Extract job title
            title_tag = job.find('p', class_='font-semibold')  # Simplified class name for title
            title = title_tag.text.strip() if title_tag else "N/A"
            titles.append(title)
            
            # Extract company name
            company_tag = job.find('p', class_='text-sm')  # Simplified class name for company
            company = company_tag.text.strip() if company_tag else "N/A"
            companies.append(company)
            
            # Extract company location
            location_tag = job.find('p', class_='text-sm')  # You might need to distinguish this differently
            location = location_tag.text.strip() if location_tag else "N/A"
            locations.append(location)
            
            # Extract job salary
            salary_tag = job.find('p', class_='text-sm')  # You might need to find a different way to distinguish this
            salary = salary_tag.text.strip() if salary_tag else "N/A"
            salaries.append(salary)

        # Ensure all lists have the same length by finding the minimum length
        min_length = min(len(titles), len(companies), len(locations), len(salaries))

        # Slice the lists to the minimum length
        titles = titles[:min_length]
        companies = companies[:min_length]
        locations = locations[:min_length]
        salaries = salaries[:min_length]

        # Combine the titles and companies into a DataFrame
        jobs_df = pd.DataFrame({
            'Job Titles': titles,
            'Company Names': companies,
            'Company Locations': locations,
            'Salary': salaries
        })

        return jobs_df

class Future_Job_Scraper:
    # URL of job portal
    url = 'https://career.adnexio.jobs/jobs/'

    @classmethod
    def scrape_jobs(cls):
        jobs_df = pd.DataFrame(
            {'Product': ['Sample_Product'],
             'Price': ['Sample_Price'],
             'Company': ['Company_Name'],
             'Location': ['Location_Product'],
             'Details': ['Details_Product']}
        )
        return jobs_df