import streamlit as st
from PIL import Image

def txtToAsl():
    st.title("ASL Practice")
    st.subheader("Practice your ASL skills with us!")
    user_input = st.text_input("Enter your input").upper()
    if user_input == 'A':
        image = Image.open('images/letter_A.jpeg')
        st.image(image, caption = 'A')
    elif user_input == 'B': 
        image = Image.open('images/letter_B.jpeg')
        st.image(image, caption = 'B')
    elif user_input == 'C':
        image = Image.open('images/letter_C.jpeg')
        st.image(image, caption = 'C')
    elif user_input == 'D': 
        image = Image.open('images/letter_D.jpeg')
        st.image(image, caption = 'D')
    elif user_input == 'E':
        image = Image.open('images/letter_E.jpeg')
        st.image(image, caption = 'E')
    elif user_input == 'F': 
        image = Image.open('images/letter_F.jpeg')
        st.image(image, caption = 'F')
    elif user_input == 'G':
        image = Image.open('images/letter_G.jpeg')
        st.image(image, caption = 'G')
    elif user_input == 'H': 
        image = Image.open('images/letter_H.jpeg')
        st.image(image, caption = 'H')
    elif user_input == 'I':
        image = Image.open('images/letter_I.jpeg')
        st.image(image, caption = 'I')
    elif user_input == 'J': 
        image = Image.open('images/letter_J.jpeg')
        st.image(image, caption = 'J')
    elif user_input == 'K':
        image = Image.open('images/letter_K.jpeg')
        st.image(image, caption = 'K')
    elif user_input == 'L': 
        image = Image.open('images/letter_L.jpeg')
        st.image(image, caption = 'L')
    elif user_input == 'M':
        image = Image.open('images/letter_M.jpeg')
        st.image(image, caption = 'M')
    elif user_input == 'N': 
        image = Image.open('images/letter_N.jpeg')
        st.image(image, caption = 'N')
    elif user_input == 'O':
        image = Image.open('images/letter_O.jpeg')
        st.image(image, caption = 'O')
    elif user_input == 'P': 
        image = Image.open('images/letter_P.jpeg')
        st.image(image, caption = 'P')
    elif user_input == 'Q':
        image = Image.open('images/letter_Q.jpeg')
        st.image(image, caption = 'Q')
    elif user_input == 'R': 
        image = Image.open('images/letter_R.jpeg')
        st.image(image, caption = 'R')
    elif user_input == 'S':
        image = Image.open('images/letter_S.jpeg')
        st.image(image, caption = 'S')
    elif user_input == 'T': 
        image = Image.open('images/letter_T.jpeg')
        st.image(image, caption = 'T')
    elif user_input == 'U':
        image = Image.open('images/letter_U.jpeg')
        st.image(image, caption = 'U')
    elif user_input == 'V': 
        image = Image.open('images/letter_V.jpeg')
        st.image(image, caption = 'V')
    elif user_input == 'W':
        image = Image.open('images/letter_W.jpeg')
        st.image(image, caption = 'W')
    elif user_input == 'X':
        image = Image.open('images/letter_X.jpeg')
        st.image(image, caption = 'X')
    elif user_input == 'Y': 
        image = Image.open('images/letter_Y.jpeg')
        st.image(image, caption = 'Y')
    elif user_input == 'Z':
        image = Image.open('images/letter_Z.jpeg')
        st.image(image, caption = 'Z')
    else: 
        st.write("invalid input")