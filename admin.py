import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import csv
from pages.Homepage import la, lb
 

class Admin:
    
    def __init__(self, username):
        self.username = username

    @staticmethod
    def __read_reviews():
        st.write(la)

    def ban_user(self, username):
        del LoginData[username]
        
    @staticmethod
    def __read_complaints():
        st.write(lb)
    @staticmethod
    def service():
        st.write("reviews")
        Admin.__read_reviews()
        st.write("complaints")
        Admin.__read_complaints()

if st.button("Service"):
    Admin.service()       


if st.button("Ban user"):
    username = st.text_input("enter the username to be banned", key = 23) 
    Admin.ban_user(username)


df = pd.read_csv('/home/preethamreddy/vscode/AUTOMARVEL/bought.csv')
df2 = df.T
df2.columns = ["sales"]
df2.insert(0,  "car model", [
    '2 Series Coupe', '4 Series Coupe', '8 Series Coupe', 'M2 Coupe', 'M4 Coupe',
    'C-Class Coupe', 'E-Class Coupe', 'S-Class Coupe', 'CLS Coupe', 'AMG GT Coupe',
    'A5 Coupe', 'S5 Coupe', 'RS 5 Coupe', 'TT Coupe', 'R8 Coupe', '911 Coupe',
    '718 Cayman', 'Panamera Coupe', 'Cayenne Coupe', 'Taycan Coupe', 'RC Coupe',
    'LC Coupe', 'F8 Tributo', '812 Superfast', 'SF90 Stradale', 'Huracan Coupe',
    'Aventador Coupe', 'Urus', '570S Coupe', '720S Coupe', 'Artura', 'Vantage',
    'DB11 Coupe', 'DBS Superleggera'
])

st.write(df2)
df2.index.name = "car model"
st.write(" graph of sales vs car model")
plt.figure(figsize=(12, 6))
plt.barh(df2.index, df2["sales"], color='skyblue')
plt.xlabel('Car Model')
plt.ylabel('sales ')
plt.title('Car Model vs Sales')
plt.tight_layout()
st.pyplot(plt)
























































































