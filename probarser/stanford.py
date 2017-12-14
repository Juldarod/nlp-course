import os, inspect

from nltk.parse.stanford import StanfordParser
from nltk.tree import Tree
from nltk.tokenize import sent_tokenize

model = '/usr/share/stanford-parser/englishPCFG.ser.gz'
jar = '/usr/share/stanford-parser/stanford-parser.jar'


def parse(input_text):
    dirname = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
    output_filename = os.path.join(dirname, 'output', 'probarser', 'output_stanford.txt')
    parser = StanfordParser(model, jar)
    raw_tree = parser.raw_parse_sents(sent_tokenize(input_text))
    stanford_tree = list_to_tree(raw_tree)
    output_file = open(output_filename, "w+")
    for i in range(len(stanford_tree)):
        output_file.write(' '.join(str(stanford_tree[i]).split()) + '\n')
    output_file.close()
    return stanford_tree


def list_to_tree(list_tree):
    new_tree = []
    s = object
    for tree in list_tree:
        for t in tree:
            s = Tree(t.label(), t)
        new_tree.append(s[0])
    return new_tree
