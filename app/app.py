# Core Pkgs
############
from tkinter import image_names
import streamlit as st 
import cv2
from PIL import Image,ImageEnhance
import numpy as np
import requests
from io import BytesIO

# Custom module:
################
from image_enhancer import enhancer # to enhance image"
from item_detector import item_detector # to detect items

# Custom function:
#################
@st.cache
def load_image(img):
	im = Image.open(img)
	return im

@st.cache
def load_url(url):
	response = requests.get(url)
	img = Image.open(BytesIO(response.content))
	return img

# Main function definition:
###########################
def main():
	"""Face Detection App"""
	# Name of the application
	st.title("Facial item detection App")

	# General Menu list
	activities = ["About", "Detection"]
	choice = st.sidebar.selectbox("Select Activity",activities)

	if choice == 'Detection':

		# Upload option
		select_option = ['URL', 'Upload']
		upload_option = st.radio("Select how to provide the image: ", select_option, key=2)

		# Image uploader
		if upload_option == select_option[1]:
			image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg'])
		elif upload_option == select_option[0]:
			url_link = st.text_input('Paste the URL here')
			#if url_link:
			#image_file = st.image(url_link, caption='test')

		# Loading image
		if (upload_option == select_option[1]) and (image_file is not None):
			our_image = load_image(image_file)
			# Showing image enhancements
			enhancer(our_image)
			st.write('image loaded!')
			# Detect items
			item_detector(our_image)
		elif (upload_option == select_option[0]) and (url_link != ''):
			our_image = load_url(url_link)
			# Showing image enhancements
			enhancer(our_image)
			st.write('image loaded!')
			# Detect items
			item_detector(our_image)

		# Showing image enhancements
		#enhancer(our_image)

	elif choice == 'About':
		# App description
		#st.title("Facial item detection App")
		st.text("This Application can enable you to:")
		st.markdown("""
					* Detect Faces
					* Detect smiles
					* Detect eyes
					* Apply a cartoon style to an image
					""")

		st.subheader("About Facial item Detection Application")
		st.markdown("Built with love with Streamlit by [Sebastien Sime](https://fr.linkedin.com/in/s-sime)")
		st.text("Sebastien SIME (ssime)")
		st.success("Just smile the app will do the rest")

	# Additionnal details
	st.sidebar.markdown("Built with love with Streamlit by [ssime](https://fr.linkedin.com/in/s-sime)")
		
# Main call:
###########
if __name__ == '__main__':
		main()	