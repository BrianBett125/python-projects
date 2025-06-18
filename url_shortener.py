import random
import string

class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.base_url = "https://short.ly/"
        self.used_codes = set()

    def _generate_code(self, length=6):
        """Generate a unique short code."""
        while True:
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            if code not in self.used_codes:
                self.used_codes.add(code)
                return code

    def shorten(self, long_url):
        """Shortens the URL and returns a short version."""
        code = self._generate_code()
        self.url_map[code] = long_url
        return self.base_url + code

    def expand(self, short_url):
        """Expands the short URL back to the original."""
        code = short_url.replace(self.base_url, "")
        return self.url_map.get(code, "URL not found.")

# Example usage
shortener = URLShortener()

# Shorten a long URL
long_url = "https://www.example.com/articles/python-url-shortener"
short_url = shortener.shorten(long_url)
print("Short URL:", short_url)

# Expand the short URL
original = shortener.expand(short_url)
print("Original URL:", original)

