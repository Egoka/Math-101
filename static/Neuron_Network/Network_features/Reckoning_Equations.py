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
    list_element, math_sig, number = [], ['+', '-', '×', '÷', '='], 0
    for i in range(0, len(training_list)):
        element = training_list[i]
        if element < 10:
            number = int((number + 0.1 * element) * 10)
            if training_list[i + 1] > 9:
                list_element.append(number)
                number = 0
        else:
            list_element.append(math_sig[element - 10])
    del number, element, training_list, i, math_sig
    list_element.pop(-1)
    list_example = copy.deepcopy(list_element)
    size = 0
    while len(list_element) > size:
        if list_element[size] == '-':
            try:
                if list_element[size + 1] >= 0:
                    list_element[size + 1] *= -1
                    size += 2
                    try:
                        if list_element[size - 3] > 0 or list_element[size - 3] <= 0:
                            list_element[size - 2] = '+'
                    except TypeError:
                        list_element.pop(size - 2)
            except TypeError:
                list_element.pop(size)
            except IndexError:
                list_element.pop(size)
        elif list_element[size] == '+' or list_element[size] == '×' or list_element[size] == '÷':
            try:
                if list_element[size + 1] == '-' or list_element[size + 1] >= 0:
                    size += 1
                else:
                    list_element.pop(size)
            except TypeError:
                list_element.pop(size)
        else:
            size += 1
    del size
    return example