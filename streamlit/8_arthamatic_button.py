import streamlit as st

if 'clicked1' not in st.session_state:
    st.session_state.clicked1=False

if 'clicked2' not in st.session_state:
    st.session_state.clicked2=True

def click_button1():
    st.session_state.clicked1=True
    st.write('ADD button clicked')

def click_button2():
    st.session_state.clicked2 =True
    st.write('SUB button clicked')

st.button('ADD',on_click=click_button1)
st.button('SUB',on_click=click_button2)

if(st.session_state.clicked1):
    st.title('addition program')
    n1=st.number_input('enter n1:')
    n2=st.number_input('enter n2:')
    sum=n1+n2
    st.info('additon of 2 int num')
    st.success(sum)

if(st.session_state.clicked2):
    st.title('Subtraction program')
    n1=st.number_input('enter n1 :')
    n2=st.number_input('enter n2 :')
    sub=n1-n2
    st.info('subsctraction of 2 int num')
    st.success(sub)