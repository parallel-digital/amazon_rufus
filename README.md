# Amazon Rufus Question Scraper

This Streamlit app extracts the "Ask Rufus" questions from the top 50 ASINs on an Amazon Best Seller page.

## How to Use
1. Paste a Best Seller Rank (BSR) URL from Amazon
2. Click "Run Scrape"
3. Download a deduplicated list of questions as Excel

## Requirements
- Python 3.8+
- Chrome and chromedriver installed

## Setup
```
pip install -r requirements.txt
streamlit run app.py
```