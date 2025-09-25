import streamlit as st
import google.generativeai as genai
from PIL import Image

# --- Konfigurasi API ---
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# --- Fungsi Analisis Gambar & Generate Prompt ---
def generate_promo_prompt(image, product_type="produk"):
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    Kamu adalah AI kreatif yang ahli membuat skrip video promosi profesional.
    Analisis gambar berikut (fokus pada produk utama), lalu buat prompt lengkap untuk Gemini Veo 3
    agar menghasilkan video promosi berdurasi 8 detik.

    Hasil wajib dalam format JSON:
    {{
      "indonesian": "Prompt lengkap Bahasa Indonesia",
      "english": "Full prompt in English"
    }}

    Format yang harus ada di setiap prompt:
    1. **Character**: deskripsi subjek utama (usia, gaya, outfit, ekspresi).
    2. **Background**: suasana lokasi, pencahayaan, detail latar.
    3. **Action**: alur adegan per detik (0-3s, 3-6s, dst) + gerakan kamera.
    4. **Dialogue**: kalimat yang diucapkan karakter (jika ada).
    5. **Voice-over**: narasi promosi profesional.
    6. **Camera Style**: close-up, zoom, panning, dll.
    7. **Lighting**: natural, cinematic, spotlight, dll.
    8. **Music**: jenis musik pengiring.
    9. **Aspect Ratio**: 9:16 (vertical, cocok TikTok/Reels).

    Fokus: promosi {product_type}.
    """

    response = model.generate_content([prompt, image])
    return response.text

# --- UI Streamlit ---
st.set_page_config(page_title="Veo3 Promo Generator", layout="centered")
st.title("📽️ AI Video Promo Prompt Generator (Veo 3)")

uploaded_file = st.file_uploader("📤 Upload gambar produk (jpg/png)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="📸 Gambar produk yang dianalisis", use_column_width=True)

    product_type = st.text_input("📝 Jenis produk (contoh: sepatu, baju, sandal)", "produk")

    if st.button("🔮 Buat Prompt Profesional"):
        with st.spinner("⏳ Sedang menganalisis gambar & membuat prompt..."):
            raw_result = generate_promo_prompt(image, product_type)

        # --- Parsing JSON output ---
        try:
            import json
            result = json.loads(raw_result)

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("🇮🇩 Prompt Bahasa Indonesia")
                st.text_area("Prompt Indonesia", result["indonesian"], height=300, key="indo")
                st.button("📋 Salin (ID)", on_click=lambda: st.session_state.update(clip_id=result["indonesian"]))

            with col2:
                st.subheader("🇬🇧 Prompt English")
                st.text_area("Prompt English", result["english"], height=300, key="eng")
                st.button("📋 Copy (EN)", on_click=lambda: st.session_state.update(clip_en=result["english"]))

            # Tampilkan konfirmasi kalau ada yang disalin
            if "clip_id" in st.session_state:
                st.success("✅ Prompt Indonesia berhasil disalin ke clipboard!")
            if "clip_en" in st.session_state:
                st.success("✅ Prompt English berhasil disalin ke clipboard!")

        except Exception as e:
            st.error("⚠️ Gagal parsing hasil dari AI. Coba lagi.")
            st.code(raw_result, language="json")
