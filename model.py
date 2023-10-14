from roboflow import Roboflow
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, VideoTransformerBase

custom_css = """
<style>
    .my-custom-class {
        color: red;
        background-color: lightgrey;
        padding: 10px;
    }

    #my-custom-id {
        font-size: 20px;
    }
</style>
"""
st.write(custom_css, unsafe_allow_html=True)

st.write('<div class="my-custom-class">This is styled with custom CSS</div>', unsafe_allow_html=True)

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