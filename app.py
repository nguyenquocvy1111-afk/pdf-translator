import streamlit as st
import fitz  # PyMuPDF
from openai import OpenAI
import tempfile

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🔥 PDF Translator ULTIMATE (Giữ format 95-99%)")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

# 🔥 GPT dịch siêu mượt
def translate(text):
    if not text.strip():
        return text
    
    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Translate to Vietnamese naturally, keep formatting."},
            {"role": "user", "content": text}
        ]
    )
    return res.choices[0].message.content

if uploaded_file:
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    if st.button("🔥 Dịch giữ nguyên layout"):
        with st.spinner("Đang xử lý cực mạnh..."):
            
            for page in doc:
                blocks = page.get_text("blocks")
                
                for b in blocks:
                    x0, y0, x1, y1, text, *_ = b
                    
                    if not text.strip():
                        continue
                    
                    vi_text = translate(text)

                    # ❌ xoá text cũ
                    page.add_redact_annot((x0, y0, x1, y1))
                    page.apply_redactions()

                    # ✅ viết text mới đúng vị trí
                    page.insert_textbox(
                        (x0, y0, x1, y1),
                        vi_text,
                        fontsize=10
                    )

            # lưu file
            temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
            doc.save(temp.name)

        with open(temp.name, "rb") as f:
            st.download_button(
                "📥 Download PDF đã dịch (Ultimate)",
                f,
                file_name="translated_ultimate.pdf"
            )
