import streamlit as st


LoginData = {"Preetham9070":"123456789Reddy", "avinash9":"12345Avi"} 
Dictnames = {"Preetham9070":"Preetham", "avinash9":"avinash"}

st.title("Sign up")
a = st.text_input("name", key = 3)
b = st.text_input("Enter Username👇", key=332)
c = st.text_input("Enter password👇", key=423)

if st.button("sign up"):
    Dictnames[b] = a
    LoginData[b] = c
    st.page_link('AUTOMARVEL/pages/loginpage.py')

