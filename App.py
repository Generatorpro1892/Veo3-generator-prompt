import streamlit as st
from google.cloud import aiplatform

# Inisialisasi Vertex AI
aiplatform.init(project="YOUR_PROJECT_ID", location="us-central1")

# Nama model Gemini yang valid
MODEL_ID = "gemini-1.5-flash"

st.set_page_config(page_title="Analisis Gambar Produk", layout="centered")

st.title("🛍️ Analisis Gambar Produk (Gemini)")

uploaded_file = st.file_uploader("Upload gambar produk (jpg/png)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Gambar produk", use_container_width=True)

    if st.button("🔍 Analisis Otomatis"):
        # Load model
        model = aiplatform.Model(model_name=f"publishers/google/models/{MODEL_ID}")

        # Buat prompt
        prompt = "Deskripsikan gambar produk ini secara singkat dalam bahasa Indonesia."

        try:
            response = model.predict(
                instances=[{
                    "content": {
                        "parts": [
                            {"mimeType": uploaded_file.type, "data": uploaded_file.getvalue()},
                            {"text": prompt}
                        ]
                    }
                }]
            )
            st.success("✅ Analisis selesai")
            st.write(response)
        except Exception as e:
            st.error(f"Gagal analisis gambar: {str(e)}")
