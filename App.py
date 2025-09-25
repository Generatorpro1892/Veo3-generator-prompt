import streamlit as st

st.title("🎬 Veo3 Prompt Generator")
st.write("Upload gambar + deskripsi → otomatis jadi prompt video promosi.")

# Upload gambar
uploaded_file = st.file_uploader("📤 Upload gambar", type=["jpg", "png", "jpeg"])

# Teks promosi
text_input = st.text_area("✍️ Tulis teks promosi", "Contoh: Promo sandal elegan, nyaman dipakai seharian.")

if uploaded_file and text_input:
    st.subheader("🔑 Prompt Final")
    prompt = f"""
    Buatkan video promosi berdurasi 8 detik.
    Analisis gambar yang diupload lalu tampilkan deskripsi visual.
    Tambahkan narasi sesuai teks berikut:
    "{text_input}"

    Gaya: cinematic, lighting realistis, suara sesuai karakter pada gambar.
    """
    st.code(prompt, language="markdown")
    st.success("✅ Prompt berhasil dibuat, siap dipakai di Veo3.")
