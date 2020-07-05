import numpy
import scipy.special


def calculation():
    training_list = numpy.load('static/Neuron_Network/Numpy_array/List_Symbol.npy')
    input_weights = numpy.load('Weight_Table_INPUT.npy')
    output_weights = numpy.load('Weight_Table_OUTPUT.npy')


def operation(input_weights, output_weights, true_input):
    true_input_t = numpy.array(true_input, ndmin=2).T  # Транспонированная картнка
    in_matrix = numpy.dot(input_weights, true_input_t)  # Входной сигнал * веса
    in_finale = activation_function(in_matrix)  # Выходной результат функции входных сигналов
    out_matrix = numpy.dot(output_weights, in_finale)  # Выходной сигнал * веса
    out_finale = activation_function(out_matrix)  # Выходной результат функции выходных сигналов
    return out_finale


###########################################################
def activation_function(x):
    return scipy.special.expit(x)  # Функция активации  f(x) = 1 / (1+e^-x ) Сигмооида