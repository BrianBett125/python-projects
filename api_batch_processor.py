import requests
import time
import logging
from functools import lru_cache, wraps

# Set up structured logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# Retry decorator for handling flaky network calls
def retry(max_retries=3, delay=2):
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

# Cached API call with retry logic
@lru_cache(maxsize=128)
@retry(max_retries=3, delay=1)
def fetch_data_from_api(query: str) -> dict:
    logging.info(f"Fetching data for query: {query}")
    url = f"https://api.example.com/data?q={query}"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()

# Batch processing
def process_queries(queries):
    results = {}
    for query in queries:
        try:
            data = fetch_data_from_api(query)
            results[query] = data
        except Exception as e:
            logging.error(f"Failed to fetch data for '{query}': {e}")
            results[query] = None
    return results

# Example usage
if __name__ == "__main__":
    queries = ["ai", "cloud", "python"]
    output = process_queries(queries)
    print(output)

