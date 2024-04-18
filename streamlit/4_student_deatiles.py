import streamlit as st

name=st.text_input('enter the name')
id=st.number_input('enter the id')
branch=st.text_input('enter the barch')

test1=st.number_input('enter 1st test marks')
test2=st.number_input('enter 2nd test marks')
test3=st.number_input('enter 3nd test marks')
avg=(test2+test1+test3)/3

st.write("Student Name:",name)
st.write("Student ID",id)
st.write("Student Branch:",branch)


st.write("Student Avearge Marks of the Test:",avg)