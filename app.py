import streamlit as st
from scraper import get_top_50_asins, extract_rufus_questions
import pandas as pd

st.title("Amazon Rufus Question Scraper")

bsr_url = st.text_input("Paste Amazon Best Seller URL:", 
                        "https://www.amazon.com/Best-Sellers-Patio-Lawn-Garden-Patio-Furniture-Cushions-Pads/zgbs/lawn-garden/553788")

if st.button("Run Scrape"):
    with st.spinner("Scraping ASINs..."):
        asins = get_top_50_asins(bsr_url)
    with st.spinner("Extracting Rufus Questions..."):
        questions = []
        for asin in asins:
            q_list = extract_rufus_questions(asin)
            questions.extend(q_list)
        unique_questions = list(set(questions))
        df = pd.DataFrame(unique_questions, columns=["Rufus Question"])
        st.success(f"Extracted {len(unique_questions)} unique questions.")
        st.dataframe(df)
        st.download_button("Download Excel", df.to_excel(index=False), "rufus_questions.xlsx")