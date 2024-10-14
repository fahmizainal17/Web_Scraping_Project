import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the IMDb Top 250 Movies page
url = 'https://www.imdb.com/chart/top/'

# Send a GET request to fetch the HTML content of the page
response = requests.get(url)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Create lists to store data
titles = []
years = []
ratings = []

# Find the containers with movie details
movies = soup.find_all('div', class_='ipc-metadata-list-summary-item__tc')

# Loop through each movie container to extract details
for movie in movies:
    # Extract title
    title = movie.find('h3', class_='ipc-title__text').text.strip()
    
    # Extract year
    year = movie.find('span', class_='cli-title-metadata-item').text.strip()
    
    # Extract rating
    rating = movie.find('span', class_='ipc-rating-star--rating').text.strip()

    # Add to the lists
    titles.append(title)
    years.append(year)
    ratings.append(rating)

# Create a DataFrame to store the movie details
df = pd.DataFrame({
    'Title': titles,
    'Year': years,
    'Rating': ratings
})

# Display the DataFrame
print(df)
