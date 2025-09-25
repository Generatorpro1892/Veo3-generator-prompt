import streamlit as st
import google.generativeai as genai
from PIL import Image

# Load API Key dari secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Fungsi analisis gambar + buat prompt profesional
def generate_promo_prompt(image, product_type="produk"):
    model = genai.GenerativeModel("gemini-1.5-flash")

    base_prompt = f"""
    Kamu adalah AI kreatif yang ahli membuat skrip video promosi profesional untuk iklan produk.
    Analisis gambar berikut (fokus pada produk utama), lalu buat prompt lengkap untuk Gemini Veo 3
    agar menghasilkan video promosi berdurasi **8 detik**.

    Format wajib:
    1. **Character**: deskripsi subjek utama (usia, gaya, penampilan, outfit).
    2. **Background**: suasana lokasi, pencahayaan, detail ruangan/latar.
    3. **Action**: alur adegan per detik (0-2s, 2-4s, 4-6s, 6-8s) dengan gerakan kamera.
    4. **Dialogue**: kalimat yang diucapkan model.
    5. **Voice-over**: narasi promosi profesional (energik, jelas).
    6. **Camera Style**: gaya pengambilan gambar (close-up, zoom, panning).
    7. **Lighting**: pencahayaan (natural, cinematic, spotlight, dll).
    8. **Music**: jenis musik pengiring.
    9. **Aspect Ratio**: 9:16 (vertical, cocok untuk TikTok/Reels).

    Pastikan hasilnya panjang, detail, profesional, dan persuasif.
    Fokus: promosi {product_type}.
    """

    # Generate versi Indonesia
    response_id = model.generate_content([base_prompt + "\nTulis dalam bahasa Indonesia.", image])

    # Generate versi English
    response_en = model.generate_content([base_prompt + "\nWrite in English.", image])

    return response_id.text, response_en.text


# UI Streamlit
st.title("📽️ AI Video Promo Prompt Generator (Veo 3)")

uploaded_file = st.file_uploader("Upload gambar produk (jpg/png)", type=["jpg","jpeg","png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar produk yang dianalisis", use_column_width=True)

    product_type = st.text_input("Jenis produk (contoh: sepatu, baju gamis, sandal)", "produk")

    if st.button("🔮 Buat Prompt Profesional (8 Detik)"):
        with st.spinner("Sedang menganalisis gambar & membuat prompt..."):
            prompt_id, prompt_en = generate_promo_prompt(image, product_type)

        # Hasil Prompt Indonesia
        st.subheader("🇮🇩 Prompt Bahasa Indonesia (8 Detik)")
        st.code(prompt_id, language="markdown")
        st.button("📋 Salin Prompt Indonesia", on_click=st.write, args=("✅ Prompt Indonesia siap disalin",))

        # Hasil Prompt English
        st.subheader("🇬🇧 Prompt English (8 Seconds)")
        st.code(prompt_en, language="markdown")
        st.button("📋 Copy English Prompt", on_click=st.write, args=("✅ English Prompt ready to copy",))
