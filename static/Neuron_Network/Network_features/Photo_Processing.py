from skimage import io
import numpy as np
import math


def translate_arr():
    photo = io.imread('static/Neuron_Network/img/paint.png')
    photo = np.sum(photo, axis=2) // photo.shape[2]
    photo = photo.astype('uint8')
    if photo.shape[0] > 1000 and photo.shape[1] > 1000:
        photo = compression(photo, int(photo.shape[0] / 2), int(photo.shape[1] / 2), False)


################################################################
def compression(photo, height_out, width_out, bypass):
    return small_photo
