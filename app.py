from deep_translator import GoogleTranslator

def translate_text(text):
    chunk_size = 4000  # nhỏ hơn 5000 cho chắc
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    
    translated_chunks = []
    
    for chunk in chunks:
        try:
            translated = GoogleTranslator(source='en', target='vi').translate(chunk)
            translated_chunks.append(translated)
        except:
            translated_chunks.append("[Lỗi dịch đoạn này]")
    
    return "\n".join(translated_chunks)
         
