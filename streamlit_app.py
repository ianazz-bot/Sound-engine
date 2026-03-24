import streamlit as st

st.title("🎛️ Sound Engine")

query = st.text_input("Enter artist + song + instrument")

if query:
    q = query.lower()

    if "every breath you take" in q:
        st.subheader("🎸 Guitar Match")
        st.write("Line 6 Clean Chorus → UAD LA-2A → Studio One EQ")

    elif "jack johnson" in q:
        st.subheader("🎸 Acoustic Match")
        st.write("Townsend Mic → UAD LA-2A → Studio One EQ")

    elif "elvis" in q:
        st.subheader("🎤 Vocal Match")
        st.write("Townsend Tube Model → UAD 1176 → LA-2A → Lexicon 224")

    else:
        st.warning("No match found")
