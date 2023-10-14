from roboflow import Roboflow
import streamlit as st

def model():
    st.title('ASL detection')

    # Roboflow integration and ASL detection code
    rf = Roboflow(api_key="07xd4Fb9Jmy0RHi57x5x")
    project = rf.workspace().project("american-sign-language-letters")
    model = project.version(6).model

    # Function to predict ASL signs
    def predict(processed_image):
        print(model.predict(processed_image, confidence=40, overlap=30).json())

    picture = st.camera_input("Take a picture")

    with open("captured_image.jpg", "wb") as f:
        f.write(picture.getbuffer())

    st.write('Image captured and saved as captured_image.jpg')

    predict("captured_image.jpg")