import inspect
import os


def make_dictionary():
    directory_name = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
    filename = os.path.join(directory_name, 'dict', 'morphan', 'lemmer-lower-2plus.txt')
    archive = open(filename)
    dictionary = []
    line = archive.readline()
    while line != '':
        # procesar línea
        # word = line.split(' ')
        # dictionary.append(word[0])
        dictionary.append(str(line).strip())
        line = archive.readline()
    return dictionary
