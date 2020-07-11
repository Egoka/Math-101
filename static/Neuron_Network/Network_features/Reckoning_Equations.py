import copy
import numpy


def count():
    training_list = numpy.load('static/Neuron_Network/Numpy_array/Symbol.npy')
    try:
        while training_list[0] > 9 and training_list[0] != 11:
            training_list = numpy.delete(training_list, 0)
        while training_list[-2] > 9:
            training_list = numpy.delete(training_list, -2)
    except IndexError:
        example = "Примера нет."
        return example
    return example