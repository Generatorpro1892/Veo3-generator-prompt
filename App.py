import streamlit as st
import google.generativeai as genai
import json

# ====== Setup API Key ======
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# ====== Fungsi analisis gambar ======
def analyze_image(image_path):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = "Deskripsikan detail orang dalam gambar ini untuk keperluan pembuatan iklan video. Fokus pada ciri fisik, pakaian, suasana."
    response = model.generate_content([prompt, image_path])
    return response.text

# ====== Fungsi generator scene ======
def generate_scenes(model_desc, product_name, n_scenes=3):
    base_prompt = f"""
    Buatkan {n_scenes} skenario video promosi berdurasi 8 detik tiap scene.
    Model/karakter harus sama dengan deskripsi ini: {model_desc}.
    Produk yang dipromosikan: {product_name}.
    
    Untuk tiap scene sertakan:
    1. Visual (aksi, lokasi, suasana, angle kamera).
    2. Narasi/voice-over singkat.
    3. Durasi = 8 detik.

    Format jawaban dalam JSON:
    {{
      "scenes": [
        {{
          "scene": 1,
          "visual": "...",
          "voiceover": "...",
          "duration": "8s"
        }},
        ...
      ]
    }}
    """
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(base_prompt)

    try:
        return json.loads(response.text)
    except:
        return {"error": "JSON parsing gagal", "raw_output": response.text}

# ====== Streamlit UI ======
st.title("🎬 Prompt Generator Otomatis (Gemini API)")

uploaded_file = st.file_uploader("📷 Upload gambar referensi model", type=["jpg", "png", "jpeg"])
product_name = st.text_input("👜 Nama produk", "Sepatu Premium")
n_scenes = st.slider("🎞️ Jumlah scene", 1, 5, 3)

if uploaded_file and st.button("🚀 Generate Prompt"):
    with st.spinner("Analisis gambar..."):
        model_desc = analyze_image(uploaded_file)

    with st.spinner("Buat skenario..."):
        scenes = generate_scenes(model_desc, product_name, n_scenes)

    st.subheader("📌 Deskripsi Model dari Gambar")
    st.write(model_desc)

    st.subheader("📌 Prompt Skenario")
    st.json(scenes)

    st.download_button(
        "💾 Download JSON",
        data=json.dumps(scenes, indent=2, ensure_ascii=False),
        file_name="scenes.json",
        mime="application/json"
    )
