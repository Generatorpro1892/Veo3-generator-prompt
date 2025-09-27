import streamlit as st
from diffusers import StableDiffusionXLImg2ImgPipeline
from PIL import Image
import torch, random, zipfile, io, os

st.set_page_config(page_title="AI Promo Generator 👡", layout="wide")
st.title("👠 AI Promo Image Generator (Format 9:16)")

# Upload produk
uploaded_file = st.file_uploader("Upload gambar produk (jpg/png)", type=["jpg", "png"])

# Jumlah scene
num_scenes = st.slider("Jumlah pose iklan:", 1, 5, 3)

# Daftar template scene
all_scenes = [
    "Wanita muda berjalan di mall, full body shot, memakai sandal dari gambar input, gaya iklan fashion profesional.",
    "Close-up kaki wanita melangkah, fokus ke sandal dari gambar input, background blur, detail produk tajam.",
    "Wanita duduk santai di sofa elegan, kaki bersilang, memakai sandal dari gambar input, gaya lifestyle.",
    "Wanita berpose di studio putih, katalog produk, fokus ke sandal dari gambar input.",
    "Street fashion style, wanita berjalan di trotoar kota modern, memakai sandal dari gambar input.",
    "Foto artistic di dalam butik fashion, sandal dari gambar input menjadi fokus utama.",
    "Wanita berdiri di taman kota, cahaya natural, memakai sandal dari gambar input.",
    "Close-up kaki wanita di lantai marmer glossy, fokus pada sandal dari gambar input.",
    "Fashion shoot dengan background pastel, lighting studio, sandal dari gambar input jelas terlihat.",
    "Outdoor photoshoot di kafe modern, wanita memakai sandal dari gambar input."
]

if uploaded_file:
    product_image = Image.open(uploaded_file).convert("RGB")

    # Load model
    pipe = StableDiffusionXLImg2ImgPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-refiner-1.0",
        torch_dtype=torch.float16
    ).to("cuda")

    # Pilih scene random
    selected_scenes = random.sample(all_scenes, num_scenes)

    results = []
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
        for idx, scene in enumerate(selected_scenes, start=1):
            with st.spinner(f"🔄 Generate Scene {idx}..."):
                result = pipe(
                    prompt=scene,
                    image=product_image,
                    strength=0.75,
                    guidance_scale=7.5,
                    height=1920,  # tinggi → 9:16
                    width=1080    # lebar → 9:16
                )
                out_img = result.images[0]
                results.append(out_img)

                # Simpan ke zip
                img_path = f"scene_{idx}.jpg"
                out_img.save(img_path)
                zip_file.write(img_path)
                os.remove(img_path)

                st.image(out_img, caption=f"Scene {idx}: {scene}", use_container_width=True)

    # Tombol download zip
    zip_buffer.seek(0)
    st.download_button(
        "⬇️ Download Semua Gambar (ZIP)",
        data=zip_buffer,
        file_name="promo_images.zip",
        mime="application/zip"
    )
