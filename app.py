import streamlit as st
from PyPDF2 import PdfReader
from deep_translator import GoogleTranslator

st.title("📄 PDF Translator (EN → VI)")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

# 🔥 Hàm chia nhỏ và dịch
def translate_text(text):
    chunk_size = 4000
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    
    translated_chunks = []
    
    for chunk in chunks:
        try:
            translated = GoogleTranslator(source='en', target='vi').translate(chunk)
            translated_chunks.append(translated)
        except:
            translated_chunks.append("[Lỗi đoạn này]")
    
    return "\n".join(translated_chunks)

if uploaded_file:
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"

    st.subheader("📌 Preview nội dung")
    st.text_area("", text[:2000], height=200)

    if st.button("Translate"):
        with st.spinner("Đang dịch..."):
            translated = translate_text(text)

        st.subheader("🇻🇳 Kết quả")
        st.text_area("", translated, height=400)

        st.download_button(
            "Download",
            translated,
            file_name="translated.txt"
        )
