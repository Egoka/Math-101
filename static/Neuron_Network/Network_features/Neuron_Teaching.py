import numpy
import scipy.special
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
    true_input_t = numpy.array(true_input, ndmin=2).T  # Транспонированная картинки
    true_output_t = numpy.array(true_output, ndmin=2).T  # Транспонированные ответы
    in_matrix = numpy.dot(input_weights, true_input_t)  # Входной сигнал * веса
    in_finale = activation_function(in_matrix)  # Выходной результат функции входных сигналов
    out_matrix = numpy.dot(output_weights, in_finale)  # Выходной сигнал * веса
    out_finale = activation_function(out_matrix)  # Выходной результат функции выходных сигналов
    del in_matrix, out_matrix
    return input_weights, output_weights


###########################################################
def activation_function(x):
    return scipy.special.expit(x)  # Функция активации  f(x) = 1 / (1+e^-x ) Сигмооида


###########################################################
def turn(image, angle):
    return ndimage.rotate(image, angle, reshape=False)
