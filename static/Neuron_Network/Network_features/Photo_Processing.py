from skimage import io
import numpy as np
import math


def translate_arr():
    photo = io.imread('static/Neuron_Network/img/paint.png')
    photo = np.sum(photo, axis=2) // photo.shape[2]
    photo = photo.astype('uint8')
    if photo.shape[0] > 1000 and photo.shape[1] > 1000:
        photo = compression(photo, int(photo.shape[0] / 2), int(photo.shape[1] / 2), False)
    photo = 255 - photo
    photo += 255 - np.amax(photo)
    limit = int(np.bincount(photo[int(photo.shape[0] / 2), :]).argmax() * 1.25)  # +25%
    i, j = 0, 0
    for row in photo:
        for column in row:
            if limit >= column:
                photo[i, j] = 0
            j += 1
        j = 0
        i += 1
    del i, j, column, row, limit
    io.imsave('static/Neuron_Network/img/paint.png', photo)


################################################################
def fragmentation():
    image = io.imread('static/Neuron_Network/img/paint.png')
    size = 28
    image = shear(image)
    one_number, row = np.zeros((1, size**2), 'int'), 0
    while image.shape[1] != row:
        if np.sum(image[:, row]) >= 300:
            row += 1
        elif row > 15:
            symbol = image[:, :row]
            symbol = shear_small(symbol)
            #########################################
            image, row = image[:, row:], 0
        else:
            image, row = image[:, row:], 0
            image = np.delete(image, row, axis=1)
    one_number = np.delete(one_number, 0, axis=0)
    np.save('app/static/Neuron_Network/Numpy_array/List_Symbol.npy', one_number)


################################################################
def shear(image):
    row = 0
    while image.shape[0] != row:
        if np.sum(image[row, :]) >= 500:
            row += 1
        elif row > 100:
            image = image[:row, :]
        else:
            image, row = image[row:, :], 0
            image = np.delete(image, row, axis=0)
    return image


################################################################
def shear_small(image):
    return image


################################################################
def compression(photo, height_out, width_out, bypass):
    height_ratio = int(photo.shape[0] / height_out)
    width_ratio = int(photo.shape[1] / width_out)
    small_photo = np.zeros((height_out, width_out), 'int')
    for i in range(0, height_out):
        n = i * height_ratio
        for j in range(0, width_out):
            h = j * width_ratio
            result = 0
            for row in photo[n:n + height_ratio, h:h + width_ratio]:
                for value in row:
                    result += value
            small_photo[i, j] = result / (height_ratio * width_ratio)
    del photo, i, j, h, n, height_ratio, width_ratio, height_out, width_out, result, value, row
    small_photo = small_photo.astype('uint8')
    ###################################
    if bypass:
        color = 255 - np.amax(small_photo)
        for i in range(0, small_photo.shape[0]):
            for j in range(0, small_photo.shape[1]):
                if small_photo[i, j] > 2:
                    small_photo[i, j] += color
    return small_photo
