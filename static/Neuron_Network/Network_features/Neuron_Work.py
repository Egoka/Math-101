import numpy
import scipy.special


def calculation():
    training_list = numpy.load('static/Neuron_Network/Numpy_array/List_Symbol.npy')
    input_weights = numpy.load('static/Neuron_Network/Numpy_array/Weight_Table_INPUT.npy')
    output_weights = numpy.load('static/Neuron_Network/Numpy_array/Weight_Table_OUTPUT.npy')
    input_str = []
    for one_photo in training_list:
        true_input = (numpy.asfarray(one_photo) / 255.0 * 0.99) + 0.01
        session = operation(input_weights, output_weights, true_input)
        if numpy.max(session) > 0.2: input_str.append(numpy.argmax(session))
    input_str.append(14)
    numpy.save('static/Neuron_Network/Numpy_array/Symbol.npy', input_str)


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