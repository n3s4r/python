import requests  # Import the requests module to handle HTTP requests
from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML
from concurrent.futures import ThreadPoolExecutor  # Import ThreadPoolExecutor for multi-threading
import urllib.robotparser  # Import robotparser to handle robots.txt rules
from urllib.parse import urlparse, urljoin  # Import urlparse and urljoin for URL manipulation

# Function to check if a URL is allowed to be scraped according to robots.txt
def is_allowed(url, user_agent='*'):
    # Parse the URL to get the base URL
    parsed_url = urlparse(url)
    base_url = f'{parsed_url.scheme}://{parsed_url.netloc}'
    robots_url = urljoin(base_url, 'robots.txt')
    
    # Parse robots.txt
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    
    # Check if the URL is allowed to be accessed
    return rp.can_fetch(user_agent, url)

# Function to fetch and parse a webpage
def fetch_page(url):
    # Check if the URL is allowed to be scraped
    if not is_allowed(url):
        print(f'Scraping not allowed for {url}')
        return None
    
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            print(f'Successfully fetched {url}')
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
        else:
            print(f'Failed to fetch {url} with status code {response.status_code}')
    except Exception as e:
        print(f'Exception occurred while fetching {url}: {e}')
    return None

# Function to extract all links from a webpage
def extract_links(soup, base_url):
    links = []
    if soup:
        # Find all anchor tags with href attribute
        for link in soup.find_all('a', href=True):
            # Resolve relative URLs
            full_url = urljoin(base_url, link['href'])
            links.append(full_url)
    return links

# Function to scrape a list of URLs using multiple threads
def scrape_urls(urls, max_workers=5):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit fetch_page tasks to the ThreadPoolExecutor
        futures = {executor.submit(fetch_page, url): url for url in urls}
        results = []
        for future in futures:
            result = future.result()
            if result:
                results.append(result)
        return results

# Main function to start the web scraper
def main():
    start_url = 'https://example.com'  # Replace with the URL you want to start scraping from
    #start_url = 'https://google.com'  # Replace with the URL you want to start scraping from
    soup = fetch_page(start_url)
    if not soup:
        return
    
    # Extract links from the start page
    links = extract_links(soup, start_url)
    # Scrape the extracted links
    pages = scrape_urls(links)
    
    # Optionally, you can further process the scraped pages
    for page in pages:
        # Example: print the title of each page
        if page:
            title = page.find('title').get_text()
            print(f'Page title: {title}')

if __name__ == '__main__':
    main()
