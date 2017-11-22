import inspect
import os


def make_dictionary():
    dirname = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
    filename = os.path.join(dirname, 'dict', 'morphan', 'lower-lemmer-2p.txt')
    archive = open(filename)
    dictionary = []
    line = archive.readline()
    while line != '':
        dictionary.append(str(line).strip())
        line = archive.readline()
    return dictionary
