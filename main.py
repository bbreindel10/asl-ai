import streamlit as st
from about import about
from resources import resources
from model import model
from txtToAsl import txtToAsl


def main():
    st.sidebar.title("Navigation")
    st.sidebar.markdown("---")

    # Create custom navigation buttons for both "About" and "Model"
    selected_page = st.sidebar.radio(" ", ["About", "Model", "Resources", "Text to ASL"])

    if selected_page == "About":
            about()
    elif selected_page == "Text to ASL":
        txtToAsl()
    elif selected_page == "Model":
        model()
    elif selected_page == "Resources":
        resources()

if __name__ == "__main__":
    main()