# Core pkgs
from PIL import Image,ImageEnhance
import streamlit as st
import cv2
import numpy as np

# custom function
def enhancer(our_image):
    #
    enhance_type = st.sidebar.radio("Enhance Type",["Original","Gray-Scale","Contrast","Brightness","Blurring"])
    #
    if enhance_type == 'Gray-Scale':
        new_img = np.array(our_image.convert('RGB'))
        img = cv2.cvtColor(new_img,1)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        st.image(gray)
    elif enhance_type == 'Contrast':
        c_rate = st.sidebar.slider("Contrast",0.5,3.5)
        enhancer = ImageEnhance.Contrast(our_image)
        img_output = enhancer.enhance(c_rate)
        st.image(img_output)
    elif enhance_type == 'Brightness':
        c_rate = st.sidebar.slider("Brightness",0.5,3.5)
        enhancer = ImageEnhance.Brightness(our_image)
        img_output = enhancer.enhance(c_rate)
        st.image(img_output)
    elif enhance_type == 'Blurring':
        new_img = np.array(our_image.convert('RGB'))
        blur_rate = st.sidebar.slider("Brightness",0.5,3.5)
        img = cv2.cvtColor(new_img,1)
        blur_img = cv2.GaussianBlur(img,(11,11),blur_rate)
        st.image(blur_img)
    elif enhance_type == 'Original':
        st.image(our_image,width=300)