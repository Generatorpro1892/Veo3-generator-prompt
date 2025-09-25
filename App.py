import streamlit as st
import json

# --- Dummy function contoh analisis ---
# Ganti ini dengan fungsi AI / Gemini kamu
def analyze_image(file):
    # Misalnya hasil AI return JSON string
    return """
    {
      "subject": "Wanita cantik",
      "action": "Memegang dan memamerkan produk",
      "expression": "Senyum percaya diri",
      "location": "Ruangan bergaya minimalis",
      "story": "Temukan kenyamanan dan gaya modern dalam setiap momen"
    }
    """

st.set_page_config(page_title="Image to Prompt", layout="centered")

st.title("🖼️ Image to Prompt Generator")

# Upload file
uploaded_file = st.file_uploader("Upload gambar", type=["jpg", "jpeg", "png"])

# Data default (kosong)
data = {"subject": "", "action": "", "expression": "", "location": "", "story": ""}

if uploaded_file:
    with st.spinner("⏳ Menganalisis gambar..."):
        try:
            analysis = analyze_image(uploaded_file)
            st.write("📊 **Hasil Analisis Mentah:**")
            st.code(analysis, language="json")

            # --- Coba parse JSON ---
            try:
                data = json.loads(analysis)
            except:
                st.warning("⚠️ Hasil analisis bukan JSON valid, silakan isi manual.")

        except Exception as e:
            st.error(f"Analisis gagal: {e}")

# --- Form detail prompt ---
st.subheader("✏️ Detail Prompt")

subject = st.text_input("Subjek Utama", value=data.get("subject", ""))
action = st.text_input("Aksi atau Aktivitas", value=data.get("action", ""))
expression = st.text_input("Ekspresi Wajah", value=data.get("expression", ""))
location = st.text_input("Lokasi", value=data.get("location", ""))
story = st.text_area("Cerita / Storytelling", value=data.get("story", ""))

# --- Gabung prompt final ---
if st.button("🔮 Generate Prompt Final"):
    final_prompt = f"""
    Subjek: {subject}
    Aksi: {action}
    Ekspresi: {expression}
    Lokasi: {location}
    Story: {story}
    """
    st.success("✅ Prompt Final Berhasil Dibuat!")
    st.code(final_prompt.strip(), language="markdown")
