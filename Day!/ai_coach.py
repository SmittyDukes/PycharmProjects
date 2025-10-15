import streamlit as st
import tempfile
from shot_analyzer import analyze_video

st.title("🏀 AI Basketball Trainer")

# File uploader
uploaded_file = st.file_uploader("Upload a training video", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    # Save uploaded file as a temp file
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    tfile.flush()

    st.info("Processing video... This may take a while.")

    # Analyze video
    stats = analyze_video(tfile.name)

    # --------------------------
    # Display results
    # --------------------------
    st.subheader("📊 Training Results")
    st.write(f"Frames Processed: {stats['frames_processed']}")
    st.write(f"Shots Detected: {stats['shots_detected']}")
    st.write(f"Makes: {stats['makes']}")
    st.write(f"Misses: {stats['misses']}")

    # Display shooting form feedback
    if "shot_scores" in stats and stats["shot_scores"]:
        st.subheader("📝 Shooting Form Feedback (sample frames)")
        for f in stats["shot_scores"][:5]:  # show first 5 examples
            st.write(f"Frame {f['frame']}: " + " | ".join(f['feedback']))
    else:
        st.write("No major form issues detected.")

    # Display processed video
    if "processed_video" in stats:
        st.subheader("🎥 Processed Video")
        st.video(stats["processed_video"])

