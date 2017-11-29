import probarser.stanford
import probarser.bikel
import os, inspect
from nltk.draw.tree import TreeView


def process_to_stanford(input_text):
    return probarser.stanford.parse(input_text)


def process_to_bikel(input_text):
    return probarser.bikel.parse(input_text)


class Processing(object):
    def __init__(self, input_text, analyzer):
        self.input_text = analyzer.pos_tagging(input_text)

    def process(self, input_text):
        stanford = process_to_stanford(input_text)
        bikel = process_to_bikel(self.input_text)
        return [stanford, bikel]

    def draw_trees(self, tree, parser, n):
        dirname = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
        filename = dirname + '/static/probarser/img/' + parser + '/output_img'
        trees = []
        cont = 1
        for t in tree[n]:
            TreeView(t)._cframe.print_to_file(filename + '%s.ps' % cont)
            os.system('convert -density 150 ' + filename + '%s.ps ' % cont + filename + '%s.png' % cont)
            cont += 1
        for i in range(cont - 1):
            trees.append('probarser/img/' + parser + '/output_img' + '%s' % (i + 1) + '.png')
        return trees
