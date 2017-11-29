import inspect
import os
from nltk.tree import Tree


def parse(input_text):
    dirname = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
    input_filename = os.path.join(dirname, 'input', 'probarser', 'input_bikel.txt')
    output_filename = os.path.join(dirname, 'output', 'probarser', 'output_bikel.txt')

    input_file = open(input_filename, "w+")
    input_file.write(input_text)
    input_file.close()

    os.system('java -server'
              ' -Xms400m -Xmx400m'
              ' -cp ' + dirname + '/dbparser/probarser/dbparser.jar:'
                                  '~/pycharm-2017.2.3/lib/bootstrap.jar:'
                                  '~/pycharm-2017.2.3/lib/extensions.jar:'
                                  '~/pycharm-2017.2.3/lib/util.jar:'
                                  '~/pycharm-2017.2.3/lib/jdom.jar:'
                                  '~/pycharm-2017.2.3/lib/log4j.jar:'
                                  '~/pycharm-2017.2.3/lib/trove4j.jar:'
                                  '~/pycharm-2017.2.3/lib/jna.jar'
                                  ' -Dparser.settingsFile='
              + dirname + '/dbparser/probarser/settings/collins.properties danbikel.parser.Parser '
                          '-is ' + dirname + '/wsj-02-21/probarser/wsj-02-21.obj.gz'
                                             ' -sa ' + input_filename +
              ' -out ' + dirname + '/output/probarser/output_bikel.txt')

    tree = []
    output_file = open(output_filename)
    raw_tree = str(output_file.readline()).strip()
    while raw_tree != '':
        tree.append(Tree.fromstring(raw_tree))
        raw_tree = str(output_file.readline()).strip()
    return tree


# os.system('python /home/juldini/PycharmProjects/nlp-course/test.py')
# os.chdir(dirname + '/dbparser/probarser/bin')
# os.system('tcsh parse 400 '
#           + dirname + '/dbparser/probarser/settings/collins.properties '
#           + dirname + '/wsj-02-21/probarser/wsj-02-21.obj.gz \\'
#           + dirname + '/input/probarser/input_bikel.txt')
# parse('((My (PRP$)) (dog (NN)) (also (RB)) (likes (VBZ)) (eating (VBG)) (sausage (NN)) (. (.)))')
