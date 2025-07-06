"""
resilient_api_client.py

A Python module for fetching data from an API with built-in caching,
retry logic, and error handling to ensure resilience in network calls.
"""

import requests
import time
import logging
from functools import lru_cache, wraps

# Set up structured logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def retry(max_retries=3, delay=2):
    """Decorator to retry a function on failure with delay."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logging.warning(f'Attempt {attempt} failed: {e}')
                    time.sleep(delay)
            raise Exception(f"All {max_retries} attempts failed.")
        return wrapper
    return decorator

@lru_cache(maxsize=128)
@retry(max_retries=3, delay=1)
def fetch_data_from_api(query: str) -> dict:
    """Fetch data from API with caching and retries."""
    logging.info(f"Fetching data for query: {query}")
    url = f"https://api.example.com/data?q={query}"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()

def process_queries(queries):
    """Process a batch of queries and return their results."""
    results = {}
    for query in queries:
        try:
            data = fetch_data_from_api(query)
            results[query] = data
        except Exception as e:
            logging.error(f"Failed to fetch data for '{query}': {e}")
            results[query] = None
    return results

if __name__ == "__main__":
    queries = ["ai", "cloud", "python"]
    output = process_queries(queries)
    print(output)

