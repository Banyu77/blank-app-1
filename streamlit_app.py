import streamlit as st

st.title("PENENTUAN KELULUSAM")
st.number_input("Masukkan nilai:")
    if number_input >=55:
        print("STATUS : LULUS)
    else:
        print("STATUS : TIDAK LULUS")
