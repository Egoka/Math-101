import numpy
from scipy import ndimage


def teach():
    out_weights = 14
    ###########################################################
    neurons = int(input('Введите число скрытых нейронов: '))
    learn = float(input('Введите скорость обучения: '))
    size = float(input('Введите размер окна нейронной сети: '))
    in_weights = size**2
    ###########################################################
    input_weights = (numpy.random.rand(neurons, in_weights) - 0.5)
    output_weights = (numpy.random.rand(out_weights, neurons) - 0.5)
    ###########################################################
    file = open('static/Neuron_Network/Mnist_Tables/mnist_train.csv', 'r')
    training_list = file.readlines()
    file.close()
    del file, neurons
    for one_photo in training_list:
        full_list = one_photo.split(',')
        true_input = (numpy.asfarray(full_list[1:]) / 255.0 * 0.99) + 0.01
        true_output = numpy.zeros(out_weights) + 0.01
        true_output[int(full_list[0])] = 0.99
        for angle in range(10, -20, -5):
            true_input = true_input.reshape(size, size)
            input_nam = turn(true_input, angle)
            input_nam = input_nam.reshape(in_weights)
            input_weights, output_weights = customization(input_weights, output_weights, input_nam, true_output, learn)


###########################################################
def customization(input_weights, output_weights, true_input, true_output, speed_learn):
    return input_weights, output_weights


###########################################################
def turn(image, angle):
    return ndimage.rotate(image, angle, reshape=False)
