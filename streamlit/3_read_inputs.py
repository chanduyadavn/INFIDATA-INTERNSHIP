import streamlit as st
n1=st.number_input('enter n1 value:')                                #cd streamlit
n2=st.number_input('enter n2 value')                                 #sreamlit run 3_read_inputs.py
if (n1>n2):
    st.info("n1 is greater than n2")
else:
    st.info("n2 is greater than n1")