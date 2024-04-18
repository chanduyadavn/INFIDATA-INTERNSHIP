import streamlit as st

add_selectbox=st.sidebar.selectbox(
   "How could you like to be  contacted?",
    ("email","home phone",'mobile phone') )

#using with noation

with st.sidebar:
    add_radio=st.radio(
        "choose a shipping method",
        ('standard(5-15 days)','express (2-5 days')
    )

    name=st.text_input('enter the customer name:')