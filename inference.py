from utils import read_yaml
import tensorflow
import tensorflow_hub
from utils import read_yaml
from constants import *
import cv2
import numpy as np
import  matplotlib.pyplot as plt
from model_preparation import model

class show_classes:
    def __init__(self,class_filepath=classes):
        self.cls=read_yaml(class_filepath)
    def show(self,image:np.array):
        image=image/255
        image=np.expand_dims(image,axis=0)
        output=model(image)
        label=np.argmax(output[0])
        xmin=int(output[1][0][0])
        ymin=int(output[1][0][1])
        xmax=int(output[1][0][2])
        ymax=int(output[1][0][3])
        return label,[xmin,ymin,xmax,ymax]


