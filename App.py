import streamlit as st

st.set_page_config(page_title="Veo3 Prompt Generator")

st.title("🎬 Veo3 Prompt Generator")
st.write("Upload gambar atau video untuk analisa otomatis, lalu hasilnya akan dibuatkan prompt video penjualan.")

# ---- Fungsi Analisa Dummy ----
def analyze_file(file):
    if file.type.startswith("image/"):
        return {
            "subject": "Produk sepatu olahraga trendi",
            "action": "Diperagakan oleh model saat berjalan",
            "expression": "Ekspresi percaya diri",
            "location": "Jalan perkotaan modern",
            "time": "Sore",
            "camera": ["Full body", "Close up produk"],
            "lighting": "Cinematic",
            "style": "Realistis",
            "mood": "Energik",
            "aspect": "9:16",
            "soundtrack": "Musik pop upbeat",
            "voice_text": "Sepatu terbaru yang nyaman dipakai seharian!",
            "language": "Indonesia",
            "voice_char": "Wanita muda",
            "extra": "Tampilkan logo brand di akhir video"
        }
    elif file.type.startswith("video/"):
        return {
            "subject": "Produk minuman sehat",
            "action": "Disajikan dalam gelas kaca",
            "expression": "Model tersenyum puas setelah minum",
            "location": "Dapur modern",
            "time": "Pagi",
            "camera": ["Close up produk", "Wide shot"],
            "lighting": "Natural",
            "style": "Cinematic",
            "mood": "Bahagia",
            "aspect": "16:9",
            "soundtrack": "Musik akustik ceria",
            "voice_text": "Segarkan harimu dengan minuman sehat ini!",
            "language": "English",
            "voice_char": "Pria dewasa",
            "extra": "Tambahkan tagline di akhir video"
        }
    else:
        return {}

# ---- Upload File Paling Atas ----
uploaded_file = st.file_uploader("Upload gambar atau video", type=["jpg", "png", "mp4"])

# ---- Analisa Otomatis ----
defaults = {}
if uploaded_file is not None:
    if uploaded_file.type.startswith("image/"):
        st.image(uploaded_file, caption="Preview gambar", use_column_width=True)
    elif uploaded_file.type.startswith("video/"):
        st.video(uploaded_file)
    defaults = analyze_file(uploaded_file)

# ---- Input Form ----
subject = st.text_input("1. Subjek Utama", value=defaults.get("subject", ""))
action = st.text_input("2. Aksi atau Aktivitas", value=defaults.get("action", ""))
expression = st.text_input("3. Ekspresi/Detail Tambahan", value=defaults.get("expression", ""))
location = st.text_input("4. Tempat/Lokasi", value=defaults.get("location", ""))
time = st.selectbox("5. Waktu (Timing)", ["Pagi", "Siang", "Sore", "Malam"], 
                    index=["Pagi","Siang","Sore","Malam"].index(defaults.get("time", "Pagi")) if defaults.get("time") else 0)
camera = st.multiselect("6. Gerakan Kamera", ["Zoom In", "Zoom Out", "Panning", "Tracking", "Close up produk", "Full body", "Wide shot"], 
                        defaults.get("camera", []))
lighting = st.selectbox("7. Pencahayaan", ["Natural", "Studio", "Dramatic", "Cinematic"], 
                        index=["Natural","Studio","Dramatic","Cinematic"].index(defaults.get("lighting", "Natural")) if defaults.get("lighting") else 0)
style = st.selectbox("8. Gaya Video", ["Realistis", "Cartoon", "Anime", "3D Render", "Cinematic"], 
                     index=["Realistis","Cartoon","Anime","3D Render","Cinematic"].index(defaults.get("style", "Realistis")) if defaults.get("style") else 0)
mood = st.selectbox("9. Suasana / Mood", ["Bahagia", "Serius", "Sedih", "Misterius", "Energik"], 
                    index=["Bahagia","Serius","Sedih","Misterius","Energik"].index(defaults.get("mood", "Bahagia")) if defaults.get("mood") else 0)
aspect = st.selectbox("10. Aspek Rasio", ["16:9", "9:16", "1:1"], 
                      index=["16:9","9:16","1:1"].index(defaults.get("aspect", "16:9")) if defaults.get("aspect") else 0)
soundtrack = st.text_input("11. Soundtrack / Musik", value=defaults.get("soundtrack", ""))
voice_text = st.text_area("12. Kalimat Voice Over", value=defaults.get("voice_text", ""))
language = st.selectbox("13. Bahasa Voice Over", ["Indonesia", "English"], 
                        index=["Indonesia","English"].index(defaults.get("language", "Indonesia")) if defaults.get("language") else 0)
voice_char = st.text_input("14. Karakter Suara", value=defaults.get("voice_char", ""))
extra = st.text_area("15. Detail Tambahan", value=defaults.get("extra", ""))
duration = st.selectbox("16. Durasi Video", ["8 detik", "15 detik", "30 detik"], index=0)  # default 8 detik

# ---- Generate Prompt ----
if st.button("Generate Prompt"):
    prompt = f"""
    🎯 Buatkan video promosi penjualan berdurasi {duration}, dengan detail berikut:

    - Subjek utama: {subject}
    - Aksi/aktivitas: {action}
    - Ekspresi: {expression}
    - Lokasi: {location}
    - Waktu: {time}
    - Gerakan kamera: {', '.join(camera)}
    - Pencahayaan: {lighting}
    - Gaya video: {style}
    - Suasana/mood: {mood}
    - Aspek rasio: {aspect}
    - Musik latar: {soundtrack}
    - Voice over: "{voice_text}" 
      (Bahasa: {language}, Karakter suara: {voice_char})
    - Detail tambahan: {extra}

    ⚡ Output berupa skrip video penjualan singkat yang padat, menarik, dan fokus pada produk.
    """

    st.success("✅ Prompt berhasil dibuat! Copy-paste ke Gemini AI:")
    st.code(prompt, language="markdown")
