import streamlit as st

def about():
    st.title('Our Mission :rocket:')

    # Add a brief introduction about the ASL practice website and its purpose
    st.write(
        "Welcome to our ASL (American Sign Language) practice website! We're passionate about inclusivity and accessibility for everyone, "
        "especially those who are hard of hearing. We've created this platform because we believe it's essential to provide resources for the Deaf community."
    )

    # Add a section explaining your motivation
    st.subheader('Our Motivation')
    st.write(
        "All too often, we see that people who are hard of hearing are expected to adapt to the preferences of those with typical hearing. "
        "But we believe that it's equally important to accommodate them and provide resources that cater to their needs. Our motivation is to bridge "
        "the gap and create a learning environment that is inclusive, supportive, and educational for all."
    )

    # Add a section about the ASL practice features
    st.subheader('Features')
    st.write(
        "Our ASL practice website offers a range of features to help you learn and practice American Sign Language effectively. These features include:"
    )
    st.markdown("- Real-time ASL detection and feedback.")
    st.markdown("- Text to ASL alphabet learning")
    st.markdown("- A supportive and encouraging community of learners.")
    st.markdown("- Resources for future ASL education.")

    # Add a closing statement
    st.write(
        "Thank you for joining us on this journey to make ASL accessible to everyone. We hope you enjoy practicing and learning sign language with us. "
        "If you have any feedback or suggestions, please feel free to reach out to us."
    )
