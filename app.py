import streamlit as st
from openai import OpenAI

# ==========================================
# KONFIGURASI API (SUDAH TERPASANG)
# ==========================================
API_KEY = "gsk_vF8mX2bN9qL5wR7tY3cZ1pJ6kH4dS0aQeUoIiA8fG5hJ2kL3mN4bV1cX0z" 
client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.groq.com/openai/v1" 
)

def tanya_ai(soal):
    try:
        prompt = f"Jawab soal berikut dengan singkat, tepat, dan langsung to the point. Jika pilihan ganda, cukup sebutkan jawabannya. Soal: {soal}"
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error AI: {str(e)}"

# ==========================================
# UI WEB APP (STREAMLIT)
# ==========================================
st.set_page_config(page_title="AutoExam AI", page_icon="🤖")
st.title("🤖 AutoExam AI")
st.write("Paste soal ujian lu di bawah, AI bakal langsung jawab.")

# Input text area untuk soal
soal_input = st.text_area("Masukkan Soal:", height=200, placeholder="Paste soal ujian di sini...")

if st.button("⚡ Jawab Otomatis", type="primary"):
    if soal_input.strip():
        with st.spinner("AI sedang berpikir..."):
            jawaban = tanya_ai(soal_input)
            
            st.success("Jawaban Ditemukan!")
            st.text_area("Hasil Jawaban:", value=jawaban, height=150)
    else:
        st.warning("Soal tidak boleh kosong!")
