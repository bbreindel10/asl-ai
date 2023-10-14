from roboflow import Roboflow
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, VideoTransformerBase

st.title('ASL detection')

rf = Roboflow(api_key="07xd4Fb9Jmy0RHi57x5x")
project = rf.workspace().project("american-sign-language-letters")
model = project.version(6).model


# infer on a local image
def predict(processed_image):
    print(model.predict(processed_image, confidence=40, overlap=30).json())

picture = st.camera_input("Take a picture")

with open("captured_image.jpg", "wb") as f:
    f.write(picture.getbuffer())

st.write('Image captured and saved as captured_image.png')

predict("captured_image.jpg")