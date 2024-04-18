import streamlit as st
import datetime

st.header("student registraion format")
my_form=st.form(key='form-1')

Fname=my_form.text_input('student first name:')
Lname=my_form.text_input('student last name:')
Email=my_form.text_input('student email :')
Mobileno=my_form.text_input('student mobile number')
Gender=my_form.radio('Gender',('male','female'))
Age=my_form.slider('age',1,100)
DOB=my_form.date_input('enter date of birth',min_value=datetime.date(1990,1,1))
Address=my_form.text_area('enter your address')
city=my_form.text_area('enter the city')
AreaPIN=my_form.text_input('enter pin')
state=my_form.text_input('state')

Qualification=['degree','masters']
Qualification=my_form.selectbox('Qualification',Qualification)


specialization1=my_form.checkbox('CS')
specialization2=my_form.checkbox('IT')
specialization3=my_form.checkbox('CA')
specialization4=my_form.checkbox('TC')

my_form.form_submit_button('SUBMIT')

st.write("first name:", Fname)
st.write("last name:", Lname)
st.write('Email:', Email)
st.write('mobilenumber:', Mobileno)
st.write('Gender:', Gender)
st.write('Age:', Age)
st.write('DOB:', DOB)
st.write('Address:', Address)
st.write('city"', city)
st.write('pin"', AreaPIN)
st.write('state:',state)
st.write('qulification:', Qualification)
#st.write("Specializations:",specialization1,specialization2,specialization3,specialization4)




