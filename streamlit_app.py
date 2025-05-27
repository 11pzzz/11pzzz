import streamlit as st

st.title("🎈 11pzzz")
st.write

st.title(“1pzzz jembaw”) 
st.header(“Mengecek Bilangan Ganjil Dan Genap”)
angka = st.number_input(“Tulis Sebuah Angka:”, value= 0, step= 1) 


if(angka % 2) == 0:
    st.write(f”{angka} Adalah Bilangan Genap”) 
else:
    st.write(f”{angka} Adalah Bilangan Ganjil”)
