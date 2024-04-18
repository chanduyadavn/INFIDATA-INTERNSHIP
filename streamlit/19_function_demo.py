import streamlit as st

st.sidebar.title('Reg form')
with st.form(key='Form1'):
    with st.sidebar:

        user_word=st.text_input('enter the keyword')
        select_language=st.radio('tweet language',('All','English','Hindi'))
        include_retweets=st.checkbox('include retweets in data')
        num_of_tweets=st.number_input('minimum number of tweets',100)
        submitted1=st.form_submit_button(label='search twitter')

st.write('keyword is:',user_word)
st.write('language is:',select_language)