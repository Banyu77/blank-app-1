import streamlit as st

st.title("PENENTUAN KELULUSAM")
nilai=st.number_input("Masukkan nilai:")
if nilai >=55:
    print("STATUS : LULUS")
else:
    print("STATUS : TIDAK LULUS")
