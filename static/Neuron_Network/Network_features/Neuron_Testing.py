import numpy


def test():
    file = open('static/Neuron_Network/Mnist_Tables/mnist_test.csv', 'r')
    training_list = file.readlines()
    file.close()
    input_weights = numpy.load('static/Neuron_Network/Numpy_array/Weight_Table_INPUT.npy')
    output_weights = numpy.load('static/Neuron_Network/Numpy_array/Weight_Table_OUTPUT.npy')