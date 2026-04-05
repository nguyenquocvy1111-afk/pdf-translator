import streamlit as st
from PyPDF2 import PdfReader
from deep_translator import GoogleTranslator

st.title("📄 PDF Translator (EN → VI)")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])


if uploaded_file:
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"

    if st.button("Translate"):
        translated = GoogleTranslator(source='en', target='vi').translate(text)
        
        st.text_area("Kết quả", translated, height=400)

        st.download_button(
            "Download",
            translated,
            file_name="translated.txt"
        )
