import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_top_50_asins(bsr_url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(bsr_url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    links = soup.select("a.a-link-normal[href*='/dp/']")
    asins = list({link['href'].split('/dp/')[1].split('/')[0] for link in links})
    return asins[:50]

def extract_rufus_questions(asin):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    url = f"https://www.amazon.com/dp/{asin}"
    driver.get(url)
    time.sleep(4)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    q_elements = soup.find_all("div", string=lambda x: x and "?" in x)
    return [el.get_text(strip=True) for el in q_elements]