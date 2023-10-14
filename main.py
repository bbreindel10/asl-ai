import streamlit as st
from about import about
from model import model

def main():
    st.sidebar.title("Navigation")
    st.sidebar.markdown("---")

    # Create custom navigation buttons for both "About" and "Model"
    selected_page = st.sidebar.radio(" ", ["About", "Model"])
    if selected_page == "About":
        about()
    elif selected_page == "Model":
        model()

if __name__ == "__main__":
    main()