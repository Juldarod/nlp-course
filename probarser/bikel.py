# ./parse 400 ~/Downloads/dbparser/settings/collins.properties ~/Downloads/wsj-02-21.obj.gz \~/Downloads/input_bikel.txt

# java -server -Xms400m -Xmx400m -cp ~/Downloads/dbparser/dbparser.jar
# -Dparser.settingsFile=~/Downloads/dbparser/settings/collins.properties \danbikel.parser.Parser -is
# ~/Downloads/wsj-02-21.obj.gz -sa ~/Downloads/input_bikel.txt

import inspect
import os
from nltk.tree import Tree


bikel_tree = Tree.fromstring('(S (NP (NNP Tokyo) (NN Ghoul)) (VP (VBZ is) (VP (VBN set) (PP (IN in) (NP (NP (DT an) ('
                             'JJ alternate) (NN reality)) (SBAR (WHADVP (WRB where)) (S (NP (NP (NNS ghouls)) (, ,'
                             ') (NP (NP (NNS individuals)) (SBAR (WHNP (WP who)) (S (VP (MD can) (ADVP (RB only)) (VP '
                             '(VB survive) (PP (IN by) (S (VP (VBG eating) (NP (JJ human) (NN flesh))))))))))) (, ,'
                             ') (VP (VBP live) (PP (IN among) (NP (DT the) (JJ normal) (NNS humans))) (PP (IN in) ('
                             'ADJP (JJ secret))) (, ,) (S (VP (VBG hiding) (NP (PRP$ their) (JJ true) (NN nature)) (S '
                             '(VP (TO to) (VP (VB evade) (NP (NN pursuit)) (PP (IN from) (NP (DT the) (NNS '
                             'authorities))))))))))))))) (. .))')


dirname = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
filename = os.path.join(dirname, 'input', 'probarser', 'input_bikel.txt')

# os.system('python /home/juldini/PycharmProjects/nlp-course/test.py')
# os.chdir(dirname + '/dbparser/probarser/bin')
# os.system('tcsh parse 400 '
#           + dirname + '/dbparser/probarser/settings/collins.properties '
#           + dirname + '/wsj-02-21/probarser/wsj-02-21.obj.gz \\'
#           + dirname + '/input/probarser/input_bikel.txt')

# os.system('java -server'
#           ' -Xms400m -Xmx400m'
#           ' -cp ' + dirname + '/dbparser/probarser/dbparser.jar:'
#                               '~/pycharm-2017.2.3/lib/bootstrap.jar:'
#                               '~/pycharm-2017.2.3/lib/extensions.jar:'
#                               '~/pycharm-2017.2.3/lib/util.jar:'
#                               '~/pycharm-2017.2.3/lib/jdom.jar:'
#                               '~/pycharm-2017.2.3/lib/log4j.jar:'
#                               '~/pycharm-2017.2.3/lib/trove4j.jar:'
#                               '~/pycharm-2017.2.3/lib/jna.jar'
#           ' -Dparser.settingsFile=' + dirname + '/dbparser/probarser/settings/collins.properties'
#           ' danbikel.parser.Parser -is ' + dirname + '/wsj-02-21/probarser/wsj-02-21.obj.gz'
#           ' -sa ' + filename +
#           ' -out ' + dirname + '/output/probarser/output_bikel.txt')
