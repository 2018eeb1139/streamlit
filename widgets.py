import streamlit as st

st.title("Widgets")

if st.button("Button"):
    st.write("Button Clicked")

username=st.text_input("Username")
st.write(username)

address=st.text_area("Address")
st.write(address)

st.date_input("Enter a Date")

st.time_input("Select your preferred Time","now")

if st.checkbox("Accept the Terms & Conditions"):
    st.write("Thanks for your time")

c1=st.radio("Colors",['r','g','b'])
c2=st.selectbox("Select Colors",['r','g','b'])

st.write(c1,c2)

c3=st.multiselect("Select Multiple Colors",['r','g','b'])
st.write(c3)

st.slider("Age",min_value=18,max_value=30)

st.number_input("Age",min_value=18.0,max_value=30.0,step=2.00)

st.file_uploader("Upload a file")