import streamlit as st
st.title("Welcome to CSM")
st.text("There are many companies thanks for choosing us")
st.text("Fill Your Form")
gmail = st.text_input("Enter Your Valid gmail : ")
Yourfirstname = st.text_input("Enter your 1st name : ")
Yourlastname = st.text_input("Enter your 2nd name : ")
Youraddress = st.text_area("Enter Your Address : ")
Yourgender = st.selectbox("Enter yor gender : ",("No","Male","Female","other"))
Button = st.button("Apply")
































































































