import streamlit as st

st.title("PENENTUAN KELULUSAM")
st.number_input("Masukkan nilai:")
nilai=int(input("Masukkan nilai:")
    if nilai>=55:
        print("STATUS : LULUS)
    else:
        print("STATUS : TIDAK LULUS")
