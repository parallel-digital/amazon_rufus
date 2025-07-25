import streamlit as st
import pandas as pd
from scraper import get_top_50_asins, extract_rufus_data
from io import BytesIO

st.title("Amazon Rufus Question Scraper v2")
bsr_url = st.text_input("Paste Amazon Best Seller URL:", 
    "https://www.amazon.com/Best-Sellers-Patio-Lawn-Garden-Patio-Furniture-Cushions-Pads/zgbs/lawn-garden/553788")

if st.button("Run Scrape"):
    with st.spinner("Scraping top 50 ASINs..."):
        asins = get_top_50_asins(bsr_url)

    all_rows = []
    with st.spinner("Extracting Rufus questions from PDPs..."):
        for asin in asins:
            rows = extract_rufus_data(asin)
            all_rows.extend(rows)

    if all_rows:
        df = pd.DataFrame(all_rows, columns=["ASIN", "Title", "Rufus Question"])
        st.success(f"Collected {len(df)} total questions across {len(asins)} ASINs.")
        st.dataframe(df)

        output = BytesIO()
        df.to_excel(output, index=False, engine='openpyxl')
        st.download_button(
            label="Download Excel",
            data=output.getvalue(),
            file_name="rufus_questions_by_asin.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.warning("No Rufus questions found.")