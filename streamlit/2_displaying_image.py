import streamlit as st
from PIL import Image
img=Image.open('img.png')
img1=Image.open('img_1.png')
st.title('Displaying Image')
st.image(img,width=750)
st.image(img1,width=750)

#in terminal
#cd streamlit
#streamlit run 2_displaying_image.py
