import cv2
import os
import mediapipe as mp
import math

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

def calculate_angle(a, b, c):
    """
    Calculate angle between three points.
    a, b, c = (x, y)
    """
    a = [a.x, a.y]
    b = [b.x, b.y]
    c = [c.x, c.y]

    ba = [a[0]-b[0], a[1]-b[1]]
    bc = [c[0]-b[0], c[1]-b[1]]
    cosine_angle = (ba[0]*bc[0] + ba[1]*bc[1]) / (math.sqrt(ba[0]**2 + ba[1]**2) * math.sqrt(bc[0]**2 + bc[1]**2) + 1e-6)
    angle = math.degrees(math.acos(max(min(cosine_angle, 1), -1)))
    return angle

def analyze_video(video_path):
    """
    Analyze basketball video for shots and shooting form using Mediapipe.
    Returns stats dictionary with:
    - frames_processed
    - shots_detected
    - makes
    - misses
    - shot_scores (frame-by-frame feedback)
    - processed_video (path to video with overlays)
    """

    if not os.path.isfile(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Could not open video file: {video_path}")

    frames_processed = 0
    shots_detected = 0
    makes = 0
    misses = 0
    shot_scores = []

    processed_video_path = "processed_video.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(processed_video_path, fourcc, fps, (width, height))

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frames_processed += 1

            # Convert BGR to RGB for Mediapipe
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            feedback = []

            if results.pose_landmarks:
                landmarks = results.pose_landmarks.landmark

                # Example: Right elbow angle
                right_elbow_angle = calculate_angle(
                    landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER],
                    landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW],
                    landmarks[mp_pose.PoseLandmark.RIGHT_WRIST]
                )

                if right_elbow_angle < 150:
                    feedback.append("Right elbow too low")
                else:
                    feedback.append("Elbow good")

                # Example: Knee angle (right)
                right_knee_angle = calculate_angle(
                    landmarks[mp_pose.PoseLandmark.RIGHT_HIP],
                    landmarks[mp_pose.PoseLandmark.RIGHT_KNEE],
                    landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE]
                )
                if right_knee_angle < 160:
                    feedback.append("Knee bent enough")
                else:
                    feedback.append("Knee too straight")

                # Draw landmarks
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Simulated shot detection (for now)
            if frames_processed % 50 == 0:
                shots_detected += 1
                if frames_processed % 100 == 0:
                    makes += 1
                    shot_result = "Made"
                else:
                    misses += 1
                    shot_result = "Missed"

                shot_score = 7 + len(feedback)  # crude score based on feedback count

                shot_scores.append({
                    "frame": frames_processed,
                    "score": shot_score,
                    "feedback": feedback
                })

                # Overlay shot result
                cv2.putText(frame, f"Shot: {shot_result}", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if shot_result=="Made" else (0,0,255), 2)

            # Overlay total shots
            cv2.putText(frame, f"Shots Detected: {shots_detected}", (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

            # Write frame
            out.write(frame)

    cap.release()
    out.release()

    stats = {
        "frames_processed": frames_processed,
        "shots_detected": shots_detected,
        "makes": makes,
        "misses": misses,
        "shot_scores": shot_scores,
        "processed_video": os.path.abspath(processed_video_path)
    }

    return stats

# Streamlit-friendly: no default video needed
if __name__ == "__main__":
    print("Use this module with Streamlit uploads:")
    print("stats = analyze_video(tfile.name)")

