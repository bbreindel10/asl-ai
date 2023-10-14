from roboflow import Roboflow
import streamlit as st

st.title('ASL detection')

rf = Roboflow(api_key="07xd4Fb9Jmy0RHi57x5x")
project = rf.workspace().project("american-sign-language-letters")
model = project.version(6).model

user_input = st.text_input("Enter your input")

# infer on a local image
def predict(image_path):
    response = model.predict(image_path, confidence=40, overlap=30).json()
    
    if 'predictions' in response:
        predictions = response['predictions']
        if predictions:
            first_prediction = predictions[0]
            if 'class' in first_prediction:
                return first_prediction['class']
    
    return None

picture = st.camera_input("Take a picture")

with open("captured_image.jpg", "wb") as f:
    f.write(picture.getbuffer())

st.write('Image captured and saved as captured_image.png')

result = predict("captured_image.jpg")

if result == None:
    st.write("Sign unclear, keep practicing!")
elif result == user_input: 
    st.write(f"You signed {user_input} correctly!")
else:
    st.write(f"Try again. You signed {user_input}, and we detected {result}")