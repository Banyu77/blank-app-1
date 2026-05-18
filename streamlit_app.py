import streamlit as st

st.title("PENENTUAN KELULUSAM")
nilai=st.number_input("Masukkan nilai:")
st.button("Hasil"):

if nilai >=55:
    print("LULUS")
else:
    print("TIDAK LULUS")
    
