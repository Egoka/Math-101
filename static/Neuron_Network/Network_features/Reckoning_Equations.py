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
    if type(list_element[0]) == str:
        list_element.pop(0)
    address, addition_address, multiplication_address, division_address = 0, 0, 0, 0
    multiplication_kay, division_kay = True, True
    while len(list_element) != 1:
        if multiplication_kay:
            try:
                multiplication_address = list_element.index('×')
            except ValueError:
                multiplication_address = 999
                multiplication_kay = False
        if division_kay:
            try:
                division_address = list_element.index('÷')
            except ValueError:
                division_address = 999
                division_kay = False
        if not division_kay and not multiplication_kay:
            try:
                address = list_element.index('+')
                list_element[address - 1] = list_element[address - 1] + list_element[address + 1]
                list_element.pop(address)
                list_element.pop(address)
                continue
            except ValueError:
                pass
        if multiplication_address > division_address:
            address = division_address
            list_element[address - 1] = round(list_element[address - 1] / list_element[address + 1], 2)
        else:
            address = multiplication_address
            list_element[address - 1] = round(list_element[address - 1] * list_element[address + 1], 2)
        list_element.pop(address)
        list_element.pop(address)
    del address, addition_address, multiplication_address, division_address, multiplication_kay, division_kay
    list_example.append('=')
    list_example.append(format(list_element[0]))
    list_example = list(map(str, list_example))
    example = ''.join(list_example)
    return example
