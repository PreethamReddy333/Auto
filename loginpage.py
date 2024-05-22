import streamlit as st
from pages.signuppage import Dictnames, LoginData
st.title("LOGIN")


class User:

    def __init__(self, name):
        self.name = name

    def logout(self):
        del self

a = st.text_input("Enter Username👇", key=1)
b = st.text_input("Enter password👇", key=2)
c = False
if LoginData.get(a) == b:
    c = True
print(c, LoginData.get(a), a)

try:
    user = User(Dictnames[a])
except:
    pass

if c == True:
   if st.button("Login"):
        user = User(Dictnames.get(a))
        st.success(f"Welcome, {user.name}!")
        st.write("You are now logged in.")
        st.page_link('/home/preethamreddy/vscode/AUTOMARVEL/pages/Homepage.py')
