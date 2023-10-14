import streamlit as st
from about import about
from model import model

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Choose a Page", ["About", "Detection"])

    if page == "About":
        about()
    elif page == "Detection":
        model()

if __name__ == "__main__":
    main()
