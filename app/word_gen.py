import requests
from collections import Counter, deque
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse, urljoin
from app.comon_words import common_words

class WordGen:
    # Common words to ignore
    common_words = common_words

    def __init__(self, url, max_words=1000, max_urls=20):
        self.url = url
        self.max_words = max_words
        self.max_urls = max_urls
        self.word_counter = Counter()
        self.visited_urls = set()
        self.domain = self._get_domain(url)
        self.url_count = 0

    def fetch_words(self):
        # Use a queue to follow links (iterative approach)
        self._scrape_page(self.url)

        # Save the results to a .txt file (with the site's name as the filename)
        filename = self._get_site_name(self.url) + ".txt"
        self._save_to_txt(filename)

    def _scrape_page(self, start_url):
        queue = deque([start_url])  # Initialize queue with the starting URL

        while queue and self.url_count < self.max_urls:
            url = queue.popleft()  # Get the next URL to process
            if url in self.visited_urls:
                continue  # Skip URLs we've already visited

            print(f"Scraping URL: {url}")
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')

                # Get all visible text
                text = soup.get_text()
                words = self._process_text(text)

                # Count word frequencies
                self.word_counter.update(words)

                # Mark this URL as visited and increase the counter
                self.visited_urls.add(url)
                self.url_count += 1

                # Follow links
                for link in soup.find_all('a', href=True):
                    next_page = link['href']
                    # Handle relative URLs and ensure it belongs to the same domain
                    full_url = urljoin(url, next_page)
                    if self._is_same_domain(full_url) and full_url not in self.visited_urls:
                        queue.append(full_url)

            except requests.RequestException as e:
                print(f"Failed to scrape {url}: {e}")

    def _process_text(self, text):
        # Remove non-alphabetical characters
        words = re.findall(r'\b\w+\b', text.lower())

        # Filter out common words
        return [word for word in words if word not in self.common_words if len(word) > 3]

    def _get_site_name(self, url):
        # Extract domain name without www
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        return domain.replace('www.', '')

    def _get_domain(self, url):
        # Extract the base domain of the starting URL
        parsed_url = urlparse(url)
        return parsed_url.netloc

    def _is_same_domain(self, url):
        # Check if the URL belongs to the same domain as the initial URL
        parsed_url = urlparse(url)
        return parsed_url.netloc == self.domain

    def _save_to_txt(self, filename):
        # Get most common words
        most_common_words = self.word_counter.most_common(self.max_words)

        # Save to a txt file and print each word added
        with open(filename, "w") as file:
            for word, count in most_common_words:
                file.write(f"{word}: {count}\n")
                print(f"Added word: '{word}' with frequency {count}")
        print(f"\nWords saved to {filename}")

