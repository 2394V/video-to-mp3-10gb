import streamlit as st
from moviepy.editor import VideoFileClip
import os

st.title("🎵 Convert Video to MP3 (Up to 10GB)")
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi", "mkv"])

if uploaded_file:
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.read())

    st.info("Processing file...")
    clip = VideoFileClip(uploaded_file.name)
    output_name = os.path.splitext(uploaded_file.name)[0] + ".mp3"
    clip.audio.write_audiofile(output_name)

    with open(output_name, "rb") as f:
        st.download_button("Download MP3", f, file_name=output_name)

    st.success("✅ Conversion complete!")
