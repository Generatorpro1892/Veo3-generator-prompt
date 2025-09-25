import streamlit as st
import google.generativeai as genai
from PIL import Image

# Konfigurasi API Key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("🎬 Veo 3 Prompt Generator (Auto + Manual Edit)")

uploaded_file = st.file_uploader("Upload gambar produk (jpg/png)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar produk", use_column_width=True)

    if st.button("🔍 Analisis Otomatis"):
        with st.spinner("Sedang menganalisis gambar..."):
            auto_prompt = model.generate_content([
                "Analisis gambar ini. Buat deskripsi singkat untuk isi form video promosi: subjek, aksi, ekspresi, tempat, waktu, kamera, pencahayaan, gaya, suasana, musik, dialog, detail tambahan.",
                image
            ]).text

        st.session_state["auto_prompt"] = auto_prompt

# Isi form (auto terisi kalau sudah dianalisis)
subjek = st.text_input("1. Subjek", st.session_state.get("auto_prompt", "Seorang model memegang produk"))
aksi = st.text_input("2. Aksi", "Menunjukkan produk ke kamera")
ekspresi = st.text_input("3. Ekspresi", "Tersenyum ramah")
tempat = st.text_input("4. Tempat", "Studio dengan latar bersih minimalis")
waktu = st.selectbox("5. Waktu", ["Pagi", "Siang", "Sore", "Malam"])
kamera = st.text_input("6. Gerakan Kamera", "Close-up lalu zoom out")
pencahayaan = st.text_input("7. Pencahayaan", "Cinematic natural light")
gaya = st.text_input("8. Gaya Video", "Modern realistis")
suasana = st.text_input("9. Suasana Video", "Enerjik dan profesional")
rasio = st.selectbox("10. Aspek Rasio", ["9:16 (Vertikal)", "16:9 (Lanskap)"])
musik = st.text_input("11. Suara/Musik", "Musik modern energik")
dialog = st.text_area("12. Kalimat yang Diucapkan", "Segera dapatkan produk terbaru kami sekarang juga!")
bahasa = st.selectbox("13. Bahasa Percakapan", ["Indonesia", "English"])
detail = st.text_area("14. Detail Tambahan", "Tambahkan animasi teks promosi di layar")

if st.button("✨ Buat Prompt Final"):
    hasil = f"""
Subjek: {subjek}
Aksi: {aksi}
Ekspresi: {ekspresi}
Tempat: {tempat}
Waktu: {waktu}
Gerakan Kamera: {kamera}
Pencahayaan: {pencahayaan}
Gaya Video: {gaya}
Suasana Video: {suasana}
Aspek Rasio: {rasio}
Suara/Musik: {musik}
Kalimat yang Diucapkan: {dialog}
Bahasa Percakapan: {bahasa}
Detail Tambahan: {detail}
    """
    st.subheader("📋 Prompt Siap Pakai")
    st.code(hasil, language="markdown")
    st.button("📋 Salin ke Clipboard", on_click=lambda: st.write("👉 Copy manual di atas (Streamlit mobile belum support auto-copy)."))
