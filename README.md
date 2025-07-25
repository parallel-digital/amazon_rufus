# Rufus Scraper with Targeted Extraction

This app pulls 'Ask Rufus' questions from top 50 ASINs using the exact container where questions are located:
- Extracts questions from <div id="dpx-nice-widget-container">
- Outputs ASIN, Product Title, and Rufus Questions

## Setup
```
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Cloud
Use app.py as entry point.