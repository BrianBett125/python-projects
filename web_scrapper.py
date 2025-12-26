import requests
from bs4 import BeautifulSoup
import csv
import concurrent.futures
import time

# URL List (Can be expanded or modified)
URLs = [
    "https://quotes.toscrape.com/page/1/",
    "https://quotes.toscrape.com/page/2/",
    "https://quotes.toscrape.com/page/3/"
]

# Function to scrape quotes from a given URL
def scrape_quotes(url):
    try:
        print(f"Scraping {url}...")
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all quote elements
        quotes = soup.find_all("div", class_="quote")
        data = []
        
        for quote in quotes:
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small", class_="author").get_text()
            tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]
            data.append([text, author, tags])

        print(f"Finished scraping {url}. Found {len(data)} quotes.")
        return data

    except requests.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return []

# Function to write scraped data to a CSV file
def save_to_csv(data):
    with open("scraped_quotes.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author", "Tags"])  # Header row
        for row in data:
            writer.writerow(row)
    print("Data saved to scraped_quotes.csv")

# Main function to handle multi-threaded scraping and saving the result
def main():
    all_data = []
    start_time = time.time()

    # Use ThreadPoolExecutor for concurrent scraping
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(scrape_quotes, URLs)

        for result in results:
            all_data.extend(result)

    # Save the combined results to a CSV file
    save_to_csv(all_data)
    end_time = time.time()
    print(f"Scraping completed in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()

