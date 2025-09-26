import streamlit as st
import google.generativeai as genai

# --- Konfigurasi API ---
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# --- Fungsi analisis gambar ---
def analyze_image(uploaded_file):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = "Deskripsikan detail orang dalam gambar ini untuk keperluan pembuatan iklan video. Fokus pada ciri fisik, pakaian, suasana."

    # baca file jadi bytes (biar tidak error TypeError)
    image_bytes = uploaded_file.read()
    image_data = {
        "mime_type": uploaded_file.type,  # contoh: "image/jpeg"
        "data": image_bytes
    }

    response = model.generate_content([prompt, image_data])
    return response.text

# --- Fungsi buat generate 3 scene ---
def generate_scenes(description):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""
    Berdasarkan deskripsi model berikut: {description}

    Buatkan 3 scene promosi video berdurasi total 8 detik.
    Format harus seperti ini (tanpa tambahan penjelasan lain):

    Scene 1:
    - Visual: [deskripsi visual detail]
    - Voice Over: [narasi singkat]

    Scene 2:
    - Visual: [deskripsi visual detail]
    - Voice Over: [narasi singkat]

    Scene 3:
    - Visual: [deskripsi visual detail]
    - Voice Over: [narasi singkat]
    """

    response = model.generate_content(prompt)
    return response.text

# --- UI Streamlit ---
st.title("🎬 Veo 3 Prompt Generator (Auto 3 Scene)")

uploaded_file = st.file_uploader("Upload gambar referensi (jpg/png)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Gambar Referensi", use_container_width=True)

    if st.button("🚀 Generate Prompt"):
        with st.spinner("Analisis gambar..."):
            description = analyze_image(uploaded_file)

        st.subheader("🔎 Hasil Analisis")
        st.write(description)

        with st.spinner("Generate 3 scene promosi..."):
            scenes = generate_scenes(description)

        st.subheader("🎬 Prompt Final (3 Scene)")
        st.write(scenes)
