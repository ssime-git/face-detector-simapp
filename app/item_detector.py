# Core Pkgs
import streamlit as st

# Custom module
from custom_functions import *

# Custom function
def item_detector(our_image):
    #
	task = ["Faces","Smiles","Eyes","Cannize","Cartonize"]
    #
	feature_choice = st.sidebar.selectbox("Find Features",task)
    #
	if st.button("Process"):
		if feature_choice == 'Faces':
			result_img,result_faces = detect_faces(our_image)
			st.image(result_img)
			st.success("Found {} faces".format(len(result_faces)))
		elif feature_choice == 'Smiles':
			result_img = detect_smiles(our_image)
			st.image(result_img)
		elif feature_choice == 'Eyes':
			result_img = detect_eyes(our_image)
			st.image(result_img)
		elif feature_choice == 'Cartonize':
			result_img = cartoonize(our_image)
			st.image(result_img)
		elif feature_choice == 'Cannize':
			result_canny = cannize_image(our_image)
			st.image(result_canny)