import cv2
import streamlit as st

camera = cv2.VideoCapture(0)
st.title("Webcam Live Feed")
run = st.checkbox('Run')
fre = st.image([])



while run:
    _, frame = camera.read()


    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    fre.image(frame)