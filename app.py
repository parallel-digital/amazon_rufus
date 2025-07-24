import streamlit as st
import pandas as pd
from scraper import get_top_50_asins, extract_rufus_questions
from io import BytesIO

st.title("Amazon Rufus Question Scraper")
bsr_url = st.text_input("Paste Amazon Best Seller URL:", 
    "https://www.amazon.com/Best-Sellers-Patio-Lawn-Garden-Patio-Furniture-Cushions-Pads/zgbs/lawn-garden/553788")

if st.button("Run Scrape"):
    with st.spinner("Scraping top 50 ASINs..."):
        asins = get_top_50_asins(bsr_url)
    all_questions = []
    with st.spinner("Extracting Rufus questions from PDPs..."):
        for asin in asins:
            questions = extract_rufus_questions(asin)
            all_questions.extend(questions)
    unique_questions = sorted(set(all_questions))
    df = pd.DataFrame(unique_questions, columns=["Rufus Question"])
    st.success(f"Extracted {len(unique_questions)} unique questions.")
    st.dataframe(df)
    from io import BytesIO

    output = BytesIO()
    df.to_excel(output, index=False, engine='openpyxl')
    st.download_button(
        label="Download Excel",
        data=output.getvalue(),
        file_name="rufus_questions.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
