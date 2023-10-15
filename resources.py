import streamlit as st 

def resources():
    st.title('Resources :old_key:')
    st.write(
        "Looking to learn more? Check out our resources down below!"
    )
    # Provide resources to be an ally
    st.subheader('How to be an Ally to the Hard of Hearing Community')
    st.markdown("- Don’t Assume Hearing Loss Makes Someone Less Capable")
    st.markdown("- Don’t Minimize Mild to Moderate Hearing Loss")
    st.markdown("- Stand up when you see injustice")

    # Provide resources to learn ASL
    st.subheader('Learning ASL')
    st.markdown("- http://www.lifeprint.com")
    st.markdown("- https://www.nad.org/resources/american-sign-language/learning-american-sign-language/")
    st.markdown("- https://www.rit.edu/ntid/aslte2/home/resources/building-asl-skills-and-knowledge")
    st.markdown("- https://www.signingsavvy.com")

    # Provide educational resources
    st.subheader('Educational Resources')
    st.markdown("- https://nationaldeafcenter.org/resources/deaf-awareness/")
    st.markdown("- https://hr.uw.edu/cfd/2023/08/28/september-is-deaf-awareness-month/")
    st.markdown("- https://www.who.int/news-room/fact-sheets/detail/deafness-and-hearing-loss")