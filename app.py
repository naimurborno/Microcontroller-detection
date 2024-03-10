import streamlit as st
import cv2
from inference import show_classes
from PIL import Image
import numpy as np
from utils import read_yaml
from constants import *

st.title("Welcome to the Microcontroller classification!")
file=st.file_uploader("Please upload your picture:")
if file is not None:
    image=Image.open(file)
    image=image.resize((128,128))
    image=np.array(image)
    label,annotations=show_classes().show(image)
    cls=read_yaml(classes)
    image=cv2.rectangle(image,(annotations[0],annotations[1]),(annotations[2],annotations[3]),(255,0,0),thickness=1)
    image = cv2.putText(image, cls.labels[label], (annotations[0], annotations[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 0, 0), 1, cv2.LINE_AA)
    image=image/255
    st.write(cls.labels[label])
    st.image(image)
    
    
