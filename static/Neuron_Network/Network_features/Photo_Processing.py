from skimage import io
import numpy as np
import math


def translate_arr():
    photo = io.imread('static/Neuron_Network/img/paint.png')
    photo = np.sum(photo, axis=2) // photo.shape[2]
    photo = photo.astype('uint8')