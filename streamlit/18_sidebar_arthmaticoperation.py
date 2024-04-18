import streamlit as st

st.title('arthametic operation')
st.markdown('please give the input')
#side bar
st.sidebar.title('select the operations')
st.sidebar.markdown('select the options accordingly:')

choice=st.sidebar.selectbox('select',('ADD','MUL'))
selected_status=st.sidebar.selectbox('select Number',options=['2N','5N'])

if choice == 'ADD':
    if selected_status=='2N':
        n1=st.number_input('enter n1:')
        n2= st.number_input('enter n2:')
        sum=n1+n2
        st.success(sum)
    elif selected_status=='3N':
        n1=st.number_input('enter n1:')
        n2= st.number_input('enter n2:')
        n3 =st.number_input('enter n3:')
        sum=n1+n2+n3
        st.success(sum)
elif choice=="MUL":
    if selected_status == '2N':
        n1 = st.number_input('enter n1:')
        n2 = st.number_input('enter n2:')
        MUL=n1*n2
        st.success(MUL)
    elif selected_status == '3N':
        n1 = st.number_input('enter n1:')
        n2 = st.number_input('enter n2:')
        n3 = st.number_input('enter n3:')
        MUL= n1 * n2 * n3
        st.success(MUL)