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

def extract_rufus_questions(asin):
    url = f"https://www.amazon.com/dp/{asin}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        elements = soup.find_all(string=re.compile(r"\?$"))
        questions = [q.strip() for q in elements if 30 <= len(q.strip()) <= 180]
        return questions
    except:
        return []