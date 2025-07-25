import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

def get_top_50_asins(bsr_url):
    response = requests.get(bsr_url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("a.a-link-normal[href*='/dp/']")
    asins = list({link['href'].split('/dp/')[1].split('/')[0] for link in links if '/dp/' in link['href']})
    return asins[:50]

def extract_rufus_data(asin):
    url = f"https://www.amazon.com/dp/{asin}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)

        if response.status_code != 200:
            print(f"[{asin}] Response status: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")

        title_tag = soup.find("span", id="productTitle")
        title = title_tag.get_text(strip=True) if title_tag else "N/A"

        container = soup.find("div", id="dpx-nice-widget-container")
        if not container:
            print(f"[{asin}] Rufus container not found.")
            return []

        question_spans = container.select("span > button > span")
        questions = [span.get_text(strip=True) for span in question_spans if span.get_text(strip=True)]

        return [(asin, title, q) for q in questions]
    except Exception as e:
        print(f"[{asin}] Exception: {e}")
        return []
import time

for asin in asins:
    rows = extract_rufus_data(asin)
    all_rows.extend(rows)
    time.sleep(1.5)  # 1.5 seconds between requests
