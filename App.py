import streamlit as st

st.set_page_config(page_title="Veo3 Prompt Generator")

st.title("🎬 Veo3 Prompt Generator")
st.write("Masukkan detail gambar/video untuk membuat prompt:")

# Input dari user
subject = st.text_input("1. Subjek Utama")
action = st.text_input("2. Aksi atau Aktivitas")
expression = st.text_input("3. Ekspresi/Detail Tambahan")
location = st.text_input("4. Tempat/Lokasi")
time = st.selectbox("5. Waktu (Timing)", ["Pagi", "Siang", "Sore", "Malam"])
camera = st.multiselect("6. Gerakan Kamera", ["Zoom In", "Zoom Out", "Panning", "Tracking"])
lighting = st.selectbox("7. Pencahayaan", ["Natural", "Studio", "Dramatic", "Cinematic"])
style = st.selectbox("8. Gaya Video", ["Realistis", "Cartoon", "Anime", "3D Render"])
mood = st.selectbox("9. Suasana / Mood", ["Bahagia", "Serius", "Sedih", "Misterius"])
aspect = st.selectbox("10. Aspek Rasio", ["16:9", "9:16", "1:1"])
soundtrack = st.text_input("11. Soundtrack / Musik")
voice_text = st.text_area("12. Kalimat Voice Over")
language = st.selectbox("13. Bahasa Voice Over", ["Indonesia", "English", "Japanese", "Spanish"])
voice_char = st.text_input("14. Karakter Suara (contoh: pria dewasa, wanita muda)")
extra = st.text_area("15. Detail Tambahan Lainnya")

# 🔹 Tambahan fitur upload
uploaded_file = st.file_uploader("Upload gambar atau video", type=["jpg", "png", "mp4"])
if uploaded_file is not None:
    if uploaded_file.type.startswith("image/"):
        st.image(uploaded_file, caption="Preview gambar", use_column_width=True)
    elif uploaded_file.type.startswith("video/"):
        st.video(uploaded_file)

# Tombol generate
if st.button("Generate Prompt"):
    prompt = f"""
    Subjek: {subject}
    Aksi: {action}
    Ekspresi: {expression}
    Lokasi: {location}
    Waktu: {time}
    Kamera: {', '.join(camera)}
    Pencahayaan: {lighting}
    Gaya: {style}
    Mood: {mood}
    Rasio: {aspect}
    Soundtrack: {soundtrack}
    Voice Over: {voice_text} ({language}, {voice_char})
    Tambahan: {extra}
    """
    st.success("Prompt berhasil dibuat!")
    st.text(prompt)
