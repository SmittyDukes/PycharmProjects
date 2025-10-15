import streamlit as st
import tempfile
from shot_analyzer import analyze_video

st.title("🏀 AI Basketball Trainer - Trainer Mode")

# Sidebar for upload and settings
st.sidebar.header("Upload & Settings")
uploaded_file = st.sidebar.file_uploader("Upload Practice Video", type=["mp4", "mov", "avi"])
player_select = st.sidebar.selectbox("Select Player", options=["Player 1", "Player 2", "Player 3"])
threshold_elbow = st.sidebar.slider("Elbow Angle Threshold", 60, 120, 70)

if uploaded_file is not None:
    # Show original video
    st.subheader("Original Video")
    st.video(uploaded_file)

    if st.button("Analyze Session"):
        # Save uploaded file to temp location for OpenCV
        tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        tfile.write(uploaded_file.read())
        tfile.flush()

        # Analyze video
        stats = analyze_video(tfile.name)

        # Player Stats Summary
        st.subheader(f"Stats for {player_select}")
        st.write(f"Frames Processed: {stats.get('frames_processed', 0)}")
        st.write(f"Shots Detected: {stats.get('shots_detected', 0)}")
        st.write(f"Makes: {stats.get('makes', 0)} | Misses: {stats.get('misses', 0)}")

        # Shooting Form Feedback
        if stats.get("shot_scores"):
            st.subheader("Shooting Form Feedback")
            for s in stats["shot_scores"][:5]:  # Show first 5 frames with feedback
                feedback_text = " | ".join(s['feedback']) if s['feedback'] else "Good form"
                st.write(f"Frame {s['frame']}: Score {s['score']}/10 | Feedback: {feedback_text}")
        else:
            st.write("No form issues detected.")

        # Show processed video safely
        processed_video_file = stats.get("processed_video")
        if processed_video_file:
            st.subheader("Processed Video with Highlights")
            st.video(processed_video_file)
        else:
            st.write("Processed video not available.")

        # Placeholder for session report download
        st.download_button("Download Session Report", data="Placeholder CSV/PDF", file_name="session_report.txt")
