import streamlit as st
from PyPDF2 import PdfReader
from googletrans import Translator

st.title("📄 PDF Translator (EN → VI)")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

translator = Translator()

if uploaded_file:
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"

    if st.button("Translate"):
        translated = translator.translate(text, src='en', dest='vi').text
        
        st.text_area("Kết quả", translated, height=400)

        st.download_button(
            "Download",
            translated,
            file_name="translated.txt"
        )
