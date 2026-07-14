import streamlit as st

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #F4F1FA;
    }

    [data-testid="stHeader"] {
        background-color: #E8DDF5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Prep-Pilot: Your AI-Powered Study Companion")
