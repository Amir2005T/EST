import streamlit as st

st.title("Roommate Diagnose Expert System")

mood = st.text_input("Please enter your roommate's mood", "Roommate is in bad mood")

if st.button("Ok"):
    if "bad mood" in mood.lower():
        st.info("Send her to karaoke!")
    else:
        st.info("Roommate is fine.")
