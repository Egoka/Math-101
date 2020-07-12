import numpy
from static.Neuron_Network.Network_features.Neuron_Work import operation


def test():
    file = open('static/Neuron_Network/Mnist_Tables/mnist_test.csv', 'r')
    training_list = file.readlines()
    file.close()
    input_weights = numpy.load('static/Neuron_Network/Numpy_array/Weight_Table_INPUT.npy')
    output_weights = numpy.load('static/Neuron_Network/Numpy_array/Weight_Table_OUTPUT.npy')
    true_result = 0
    for one_photo in training_list:
        full_list = one_photo.split(',')
        true_input = (numpy.asfarray(full_list[1:]) / 255.0 * 0.99) + 0.01
        session = operation(input_weights, output_weights, true_input)
        if int(full_list[0]) == numpy.argmax(session): true_result += 1
    print(len(training_list), " тестовых фотографий")
    print('Эфективность сети = ', format(((true_result / len(training_list)) * 100), '.2f'), '%')