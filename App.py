import streamlit as st

st.set_page_config(page_title="Veo3 Prompt Generator", layout="wide")

st.title("🎬 Veo3 Prompt Generator")
st.write("Masukkan detail gambar lalu dapatkan prompt video otomatis")

# Input dari user
subject = st.text_input("1. Subjek (Subject)", "Contoh: seorang nenek duduk di kursi")
action = st.text_input("2. Aksi (Action)", "Contoh: sedang minum teh hangat")
expression = st.text_input("3. Ekspresi (Expression)", "Contoh: tersenyum hangat")
location = st.text_input("4. Tempat (Location)", "Contoh: di teras rumah sederhana")
time = st.selectbox("5. Waktu (Time)", ["Pagi", "Siang", "Sore", "Malam"])
camera = st.multiselect("6. Gerakan Kamera", ["Static Shot","Pan","Tilt","Zoom In","Zoom Out","Tracking Shot","Orbit"])
lighting = st.selectbox("7. Pencahayaan (Lighting)", ["Natural Light","Studio Light","Low Light","Cinematic Lighting"])
style = st.selectbox("8. Gaya Video (Video Style)", ["Realistic","Cinematic","Documentary","Artistic"])
mood = st.selectbox("9. Suasana Video", ["Energetic","Calm","Romantic","Dramatic","Inspirational"])
aspect = st.selectbox("10. Aspek Rasio", ["16:9","9:16","4:3","21:9"])
soundtrack = st.text_input("11. Suara/Musik (Soundtrack)", "Contoh: musik lembut instrumental")
voice_text = st.text_area("12. Kalimat Promosi (Spoken Text)", "Nyaman dipakai, elegan di setiap langkah.")
language = st.selectbox("13. Bahasa (Language)", ["Indonesia","English","Jawa","Sunda"])
voice_char = st.text_input("16. Karakter Suara", "Contoh: suara nenek lembut")
extra = st.text_area("14. Detail Tambahan", "Efek cahaya lembut, transisi halus")
focus = st.text_area("18. Fokus Promosi", "Ajak audiens untuk membeli atau mencoba produk")

if st.button("🚀 Generate Prompt"):
    prompt = f"""
    🎬 **PROMPT VIDEO VEo3**
    1. Subjek: {subject}
    2. Aksi: {action}
    3. Ekspresi: {expression}
    4. Tempat: {location}
    5. Waktu: {time}
    6. Gerakan Kamera: {", ".join(camera)}
    7. Pencahayaan: {lighting}
    8. Gaya Video: {style}
    9. Suasana: {mood}
    10. Aspek Rasio: {aspect}
    11. Musik: {soundtrack}
    12. Kalimat Promosi: "{voice_text}"
    13. Bahasa: {language}
    14. Detail Tambahan: {extra}
    16. Karakter Suara: {voice_char}
    17. Sinkronisasi Bibir: Ya (lip-sync sesuai kalimat promosi)
    18. Fokus Promosi: {focus}
    """
    st.success("✅ Prompt berhasil dibuat!")
    st.code(prompt, language="markdown")
