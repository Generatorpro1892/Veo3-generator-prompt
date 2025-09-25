       import streamlit as st
import google.generativeai as genai

# Konfigurasi API Gemini dari Streamlit Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(page_title="Veo3 Prompt Generator", layout="centered")

st.title("🎬 Veo3 Prompt Generator")
st.write("Upload gambar untuk analisis otomatis. Hasil bisa diedit sebelum membuat prompt final.")

# ---- Upload File ----
uploaded_file = st.file_uploader("📤 Upload gambar produk atau model", type=["jpg", "jpeg", "png"])

# Fungsi Analisis Gambar dengan Gemini
def analyze_image(file):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = """
    Analisis detail gambar ini untuk pembuatan video promosi.
    Berikan hasil dalam format JSON dengan struktur berikut:
    {
      "subject": "subjek utama",
      "action": "aksi atau aktivitas",
      "expression": "ekspresi atau detail tambahan",
      "location": "lokasi atau setting",
      "story": "narasi singkat promosi sesuai gambar"
    }
    """
    result = model.generate_content([prompt, file])
    return result.text

# Jika ada gambar diupload → analisis
data = {"subject": "", "action": "", "expression": "", "location": "", "story": ""}
if uploaded_file:
    with st.spinner("⏳ Menganalisis gambar dengan Gemini..."):
        try:
            analysis = analyze_image(uploaded_file)
            st.write("📊 **Hasil Analisis Mentah:**")
            st.code(analysis, language="json")
        except Exception as e:
            st.error(f"Analisis gagal: {e}")

# ---- Form Input (auto terisi kalau analisis berhasil, bisa diedit manual) ----
st.subheader("✏️ Detail Prompt")
subject = st.text_input("Subjek Utama", data["subject"])
action = st.text_input("Aksi atau Aktivitas", data["action"])
expression = st.text_input("Ekspresi/Detail Tambahan", data["expression"])
location = st.text_input("Tempat/Lokasi", data["location"])
story = st.text_area("Narasi Promosi", data["story"])

# Pilihan durasi
duration = st.selectbox("Durasi Video", ["8 detik", "15 detik", "30 detik"])

# ---- Generate Prompt ----
if st.button("🚀 Buat Prompt Final"):
    prompt_final_id = f"""
Buatkan video promosi berdurasi {duration}.

Subjek: {subject}
Aktivitas: {action}
Ekspresi/Detail: {expression}
Lokasi: {location}

Narasi promosi (bahasa Indonesia atau Inggris sesuai natural):
{story}
"""
    st.success("✅ Prompt berhasil dibuat!")
    st.text_area("Prompt Final", prompt_final_id, height=300)             
