import streamlit as st
from about import about
from resources import resources
from model import model
from txtToAsl import txtToAsl


def main():
    st.sidebar.title("ASL AI " + ":i_love_you_hand_sign:")
    st.sidebar.markdown("---")

    # Create custom navigation buttons for both "About" and "Model"
    selected_page = st.sidebar.radio(" ", ["Our Mission", "ASL Detection", "Text to ASL", "Resources"])

    if selected_page == "Our Mission":
            about()
    elif selected_page == "Text to ASL":
        txtToAsl()
    elif selected_page == "ASL Detection":
        model()
    elif selected_page == "Resources":
        resources()

if __name__ == "__main__":
    main()