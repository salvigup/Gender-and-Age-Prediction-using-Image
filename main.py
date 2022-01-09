import streamlit as st
from PIL import Image
import cv2
import numpy as np
from AgeGender import scanImage, scanVideo

st.title("Age And Gender Prediction Using Image")
st.image('aaaa.jpg', use_column_width=True)


sidebar = st.sidebar

sidebar.title('User Option')


def introduction():
    st.markdown(""" Age and gender information are very important for various real world applications, such as social understanding, biomet- rics, identity verification, video surveillance, human-computer interaction, electronic customer, crowd behavior analysis, on- line advertisement, item recommendation, and many more """)

    st.subheader('Computer Vision')
    st.markdown("""Computer vision is a field of artificial intelligence (AI) that enables computers and systems to derive meaningful information from digital images, videos and other visual inputs — and take actions or make recommendations based on that information.""")
    st.image('computer.jpg', use_column_width=True)
    c1, c2 = st.columns(2)

    c1.header("Uses")
    st.markdown(""" 
        1 - The objective of this project is to classify the gender and age of an individual in real time. 

        2 - A real time Gender and Age prediction is a challenging problem when compared to other tasks in computer vision. ... The age classifier restores a whole number speaking to the age scope of the person.

      """)
    


def detect_image():
        
    image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])
    img_name = st.text_input('image.jpg')
    btn = st.button("Predict")

    if btn and image_file:
        try:
            c1, c2 = st.columns(2)
            img = Image.open(image_file)
            c1.image(img)
            img.save(f"uploads/{img_name}.png", img.format)
            with st.spinner("Predicting... Please Wait ... "):
                pre_img = scanImage(f"uploads/{img_name}.png")
                c2.image(pre_img)
            


        except Exception as e:
            print(e)
            st.error('Error Uploading Image')

def detect_webcam():
    run = st.checkbox('Start Detection')
    if run:
        scanVideo()

options = ['Project Introduction', 'Detect from Image', 'Detect from Webcam',]

selOption = sidebar.selectbox("Select an OPtion", options)

if selOption == options[0]:
    introduction()
elif selOption == options[1]:
    detect_image()
elif selOption == options[2]:
    detect_webcam()