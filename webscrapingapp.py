import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = 'https://quotes.toscrape.com/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the elements that contain the quotes and their authors
    quote_divs = soup.find_all('div', class_='quote')
    
    # Loop through the quote elements and extract information
    for quote_div in quote_divs:
        # Extract the text of the quote
        quote_text = quote_div.find('span', class_='text').text
        
        # Extract the author of the quote
        author = quote_div.find('small', class_='author').text
        
        # Extract the tags associated with the quote
        tags = [tag.text for tag in quote_div.find_all('a', class_='tag')]
        
        # Print the quote, author, and tags
        print(f'Quote: {quote_text}')
        print(f'Author: {author}')
        print(f'Tags: {", ".join(tags)}')
        print()
else:
    print(f'Failed to retrieve the web page. Status code: {response.status_code}')
