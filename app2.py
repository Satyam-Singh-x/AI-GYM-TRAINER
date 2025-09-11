import streamlit as st
import cv2
import numpy as np
import time
import PoseModule as pm
from PIL import Image

st.set_page_config(page_title="💪 Dumbbell Curl Counter", layout="wide")

st.title("💪 Virtual Dumbbell Curl Counter")

# Initialize session state
if 'count_left' not in st.session_state:
    st.session_state.count_left = 0
    st.session_state.count_right = 0
    st.session_state.dir_left = 0
    st.session_state.dir_right = 0
    st.session_state.ptime = 0

detectorPose = pm.poseDetector()
cap = cv2.VideoCapture(0)
frame_window = st.image([])

while True:
    success, img = cap.read()
    if not success:
        st.warning("Could not access webcam.")
        break

    img = cv2.flip(img, 1)
    img = detectorPose.findPose(img, draw=False)
    lmlist = detectorPose.findPosition(img, draw=False)

    if len(lmlist) != 0:
        # Right arm
        angleright = detectorPose.findAngle(img, 12, 14, 16)
        perright = np.interp(angleright, (160, 320), (0, 100))
        barright = np.interp(angleright, (160, 320), (400, 100))

        colorr = (0, 0, 255)
        if perright == 100:
            colorr = (0, 255, 0)
            if st.session_state.dir_right == 0:
                st.session_state.count_right += 0.5
                st.session_state.dir_right = 1
        if perright == 0:
            colorr = (0, 0, 255)
            if st.session_state.dir_right == 1:
                st.session_state.count_right += 0.5
                st.session_state.dir_right = 0

        cv2.rectangle(img, (10, 100), (50, 400), colorr, 2)
        cv2.rectangle(img, (10, int(barright)), (50, 400), colorr, cv2.FILLED)
        cv2.putText(img, f'RIGHT CURLS: {int(st.session_state.count_right)}',
                    (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, colorr, 2)

        # Left arm
        angleleft = detectorPose.findAngle(img, 11, 13, 15)
        perleft = np.interp(angleleft, (40, 190), (0, 100))
        barleft = np.interp(angleleft, (40, 190), (100, 400))

        colorl = (0, 0, 255)
        if perleft == 0:
            colorl = (0, 255, 0)
            if st.session_state.dir_left == 0:
                st.session_state.count_left += 0.5
                st.session_state.dir_left = 1
        if perleft == 100:
            colorl = (0, 0, 255)
            if st.session_state.dir_left == 1:
                st.session_state.count_left += 0.5
                st.session_state.dir_left = 0

        cv2.rectangle(img, (550, 100), (600, 400), colorl, 2)
        cv2.rectangle(img, (550, int(barleft)), (600, 400), colorl, cv2.FILLED)
        cv2.putText(img, f'LEFT CURLS: {int(st.session_state.count_left)}',
                    (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, colorl, 2)

    # Show FPS
    ctime = time.time()
    fps = 1 / (ctime - st.session_state.ptime)
    st.session_state.ptime = ctime
    cv2.putText(img, f'FPS: {int(fps)}', (200, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    frame_window.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

cap.release()
