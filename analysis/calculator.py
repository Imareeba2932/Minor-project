import streamlit as st

st.title("CALCULATOR")
st.markdown('Welcome To My First  Streamlit App 🤣')

c1 , c2=st.columns(2)
fnum = c1.number_input('enter first number')
snum = c2.number_input('enter first number')

options =["Add","Sub","Mul","Div"]
choice = st.radio("Select an operation", options,horizontal=True)

button = st.button('Calculate')

if button:
    if choice == "Add":
        result=fnum+snum
    if choice == "Sub":
        result=fnum-snum
    if choice == "Mul":
        result=fnum*snum
    if choice == "Div":
        result=fnum/snum
st.success(f"result is {result}")
