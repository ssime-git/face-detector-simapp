# Core Pkgs
from turtle import color
import cv2
import numpy as np

# CV2 dependencies
face_cascade = cv2.CascadeClassifier('cv2_dep_frecog/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('cv2_dep_frecog/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('cv2_dep_frecog/haarcascade_smile.xml')

# Custom function to convert en transform image
def convert_nd_transform(image):
    # Convert to RGB
    new_img = np.array(image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    # Transform to gray scale
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    return img, gray

# Custom functions to detect faces
def detect_faces(input_image):
    """Detect face on a picture
    INPUT: uploaded image
    OUTPUT: image + box around faces
    """
    # Get the transformation
    img, gray = convert_nd_transform(input_image)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle on image
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    return img, faces

# Custom function to detect eyes
def detect_eyes(input_image):
    """Detect face on a picture
    INPUT: uploaded image
    OUTPUT: image + box around eyes
    """
    # Get the transformation
    img, gray = convert_nd_transform(input_image)

    # Detect eyes
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw rectangle around eyes
    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    return img

# Custom function to detect smiles
def detect_smiles(input_image):
    """Detect face on a picture
    INPUT: uploaded image
    OUTPUT: image + box around smiles
    """
    # Get the transformation
    img, gray = convert_nd_transform(input_image)

    # Detect smiles
    smiles = smile_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around smiles
    for (x, y, w, h) in smiles:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    return img

# Custom function to cartoonize
def cartoonize(input_image):
    """Detect face on a picture
    INPUT: uploaded image
    OUTPUT: image cartonized
    """
    # Get the transformation
    img, gray = convert_nd_transform(input_image)

    # Detect edges
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Adapt colors
    color = cv2.bilateralFilter(img, 9, 300, 300)

    # Transform to cartoon
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon

# Custom function
def cannize_image(input_image):
	new_img = np.array(input_image.convert('RGB'))
	img = cv2.cvtColor(new_img,1)
	img = cv2.GaussianBlur(img, (11, 11), 0)
	canny = cv2.Canny(img, 100, 150)
	return canny