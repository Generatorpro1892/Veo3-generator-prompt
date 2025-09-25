import streamlit as st

st.title("🎬 Veo 3 Prompt Generator")

subjek = st.text_input("1. Subjek", "Seorang kakek Indonesia berambut putih")
aksi = st.text_input("2. Aksi", "Sedang memegang sepatu promosi")
ekspresi = st.text_input("3. Ekspresi", "Wajahnya tersenyum ramah")
tempat = st.text_input("4. Tempat", "Di pasar tradisional")
waktu = st.selectbox("5. Waktu", ["Pagi", "Siang", "Sore", "Malam"])
kamera = st.text_input("6. Gerakan Kamera", "Close-up lalu zoom out")
pencahayaan = st.text_input("7. Pencahayaan", "Natural cinematic")
gaya = st.text_input("8. Gaya Video", "Realistis modern")
suasana = st.text_input("9. Suasana Video", "Hidup dan ceria")
rasio = st.selectbox("10. Aspek Rasio", ["9:16 (Vertikal)", "16:9 (Lanskap)"])
musik = st.text_input("11. Suara/Musik", "Musik energik modern")
dialog = st.text_area("12. Kalimat yang Diucapkan", "Ayo buruan, sepatu terbaru ini bikin langkahmu percaya diri!")
bahasa = st.selectbox("13. Bahasa Percakapan", ["Indonesia", "English"])
detail = st.text_area("14. Detail Tambahan", "Tambahkan animasi teks promosi di bagian bawah layar")

if st.button("✨ Buat Prompt"):
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
