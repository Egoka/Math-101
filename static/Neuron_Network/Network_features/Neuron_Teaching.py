import numpy


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