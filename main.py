import streamlit as st
from PIL import Image
import cv2
import numpy as np
from AgeGender import scanImage

st.title("My Mini Project")
st.image('hero.jpg', use_column_width=True)


sidebar = st.sidebar

sidebar.title('User Option')


def introduction():
    st.markdown("""
         ## Heading Level 2
         - Feature 1
         - Feature 2
         - Feature 3
    """)
    c1, c2 = st.columns(2)

    c1.header("Column 1 Content")
    c2.header("Column 2 Content")


def execute():
    st.subheader('project working here')


options = ['Project Introduction', 'Execution']

selOption = sidebar.selectbox("Select an OPtion", options)

if selOption == options[0]:
    introduction()
elif selOption == options[1]:
    execute()
    

image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])
img_name = st.text_input("Enter image name")
btn = st.button("Predict")

if btn and image_file:
    img = Image.open(image_file)
    st.image(img)
    img.save(f"uploads/{img_name}.png", img.show)