import datetime

import streamlit as st
st.header("student registraion format")
my_form=st.form(key='form-1')

#fname lname email mobileno age gender dob addres upload resume
Fname=my_form.text_input('student first name:')
Lname=my_form.text_input('student last name:')
Email=my_form.text_input('student email :')
Mobileno=my_form.text_input('student mobile number')
Gender=my_form.radio('Gender',('male','female'))
Age=my_form.slider('age',1,100)
DOB=my_form.date_input('enter date of birth',min_value=datetime.date(1990,1,1))
Address=my_form.text_area('enter your address')
uplodresume=my_form.file_uploader('upload ur resume')
my_form.form_submit_button('SUBMIT')

st.write("first name",Fname)
st.write("last name",Lname)
st.write('Email',Email)
st.write('mobilenumber',Mobileno)
st.write('Gender',Gender)
st.write('Age',Age)
st.write('DOB',DOB)
st.write('Address',Address)