import threading
import requests
import re
import time
import logging
from queue import Queue
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

# Plugin base class
class Plugin:
    def on_response(self, url, response):
        """Override this to process the response from a URL"""
        pass

class EmailExtractorPlugin(Plugin):
    def on_response(self, url, response):
        emails = set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", response.text))
        for email in emails:
            logging.info(f"[Plugin] Found email on {url}: {email}")

class WebCrawler:
    def __init__(self, base_url, max_threads=5, plugins=None):
        self.base_url = base_url
        self.visited = set()
        self.queue = Queue()
        self.lock = threading.Lock()
        self.max_threads = max_threads
        self.plugins = plugins or []

        # Enqueue base URL
        self.queue.put(base_url)

    def fetch_url(self, url):
        """Fetch the content of a URL using requests."""
        try:
            headers = {"User-Agent": "CustomWebCrawler/1.0"}
            response = requests.get(url, headers=headers, timeout=10)
            return response
        except Exception as e:
            logging.warning(f"[Crawler] Failed to fetch {url}: {e}")
            return None

    def extract_links(self, base_url, html):
        """Extract all links from a page."""
        soup = BeautifulSoup(html, 'html.parser')
        links = set()
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            joined_url = urljoin(base_url, href)
            if self.base_url in joined_url:  # Only crawl within domain
                links.add(joined_url.split('#')[0])
        return links

    def crawl(self):
        """Worker function for crawling."""
        while True:
            try:
                url = self.queue.get(timeout=5)
            except:
                return

            with self.lock:
                if url in self.visited:
                    continue
                self.visited.add(url)

            logging.info(f"[Crawler] Visiting: {url}")
            response = self.fetch_url(url)

            if response and response.status_code == 200:
                # Plugin execution

