import streamlit as st
import replicate
from PIL import Image
import io

st.set_page_config(page_title="AI Product Promo", layout="centered")

st.title("👠 AI Product Promo Generator (9:16)")

# API Key
replicate_api = st.text_input("🔑 Masukkan Replicate API Key:", type="password")

# Upload produk
uploaded_file = st.file_uploader("📤 Upload gambar produk (sandal/sepatu)", type=["jpg", "jpeg", "png"])

# Prompt pose
prompt_pose = st.text_area("📝 Prompt pose/model:", 
                           "Seorang wanita cantik berjalan di mall, tampilan full body, proporsi realistis, background ramai.")

if st.button("🚀 Generate Gambar"):
    if not replicate_api:
        st.error("Masukkan dulu Replicate API Key kamu.")
    elif not uploaded_file:
        st.error("Upload dulu gambar produk.")
    else:
        client = replicate.Client(api_token=replicate_api)
        
        # Baca gambar
        image = Image.open(uploaded_file)
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)

        with st.spinner("Sedang generate..."):
            output = client.run(
                "stability-ai/sdxl:9d21e6c0a9c9d3f69b1a661d5af0b1b5cc7c4bde6cf454a5b7cc2b6a3f58bfe7",
                input={
                    "prompt": prompt_pose,
                    "image_dimensions": "576x1024",   # format 9:16
                    "num_outputs": 1,
                    "num_inference_steps": 30,
                    "guidance_scale": 7.5
                }
            )

        st.image(output[0], caption="Hasil Gambar (9:16)", use_container_width=True)
        st.success("✅ Selesai!")
