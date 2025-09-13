💪 Virtual Dumbbell Curl Counter

A real-time, AI-powered dumbbell curl counter using computer vision and pose estimation. This Streamlit app tracks your left and right arm curls, displays live progress, and shows completion percentage and FPS. Perfect for fitness enthusiasts, trainers, and home workouts.

Features

✅ Tracks left and right arm dumbbell curls simultaneously.

✅ Counts repetitions automatically using pose estimation.

✅ Displays real-time progress bars and percentage completion.

✅ Shows FPS for performance monitoring.

✅ Stylish, interactive Streamlit interface.


Installation

Clone the repository:

git clone https://github.com/Satyam-Singh-x/AI-GYM-TRAINER.git

cd AI-GYM-TRAINER


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py

Requirements

Python 3.8+

OpenCV

NumPy

Mediapipe

Streamlit

Pillow

Usage

Run the Streamlit app.

Allow webcam access.

Perform dumbbell curls in front of the camera.

Track your left and right curls in real-time on the dashboard.

Project Structure
virtual-dumbbell-counter/
│
├─ app.py                  # Main Streamlit app

├─ PoseModule.py           # Pose estimation module

├─ requirements.txt        # Python dependencies

└─ README.md

Future Improvements

Add exercise detection for other workouts (squats, push-ups, etc.).

Save workout history to a file or database.

Add color themes and more stylish UI elements.

License

MIT License © 2025

Created by Satyam

Mail: singhsatyam.0912@gmail.com
