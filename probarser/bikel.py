# ./parse 400 ~/Downloads/dbparser/settings/collins.properties ~/Downloads/wsj-02-21.obj.gz \~/Downloads/input_bikel.txt

# java -server -Xms400m -Xmx400m -cp ~/Downloads/dbparser/dbparser.jar
# -Dparser.settingsFile=~/Downloads/dbparser/settings/collins.properties \danbikel.parser.Parser -is
# ~/Downloads/wsj-02-21.obj.gz -sa ~/Downloads/input_bikel.txt

import inspect
import os

dirname = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
filename = os.path.join(dirname, 'input', 'probarser', 'input_bikel.txt')

# os.system('python /home/juldini/PycharmProjects/nlp-course/test.py')
# os.chdir(dirname + '/dbparser/probarser/bin')
# os.system('tcsh parse 400 '
#           + dirname + '/dbparser/probarser/settings/collins.properties '
#           + dirname + '/wsj-02-21/probarser/wsj-02-21.obj.gz \\'
#           + dirname + '/input/probarser/input_bikel.txt')

os.system('java -server -Xms400m -Xmx400m -cp '
          + dirname + '/dbparser/probarser/dbparser.jar:'
                      '~/pycharm-2017.2.3/lib/bootstrap.jar:'
                      '~/pycharm-2017.2.3/lib/extensions.jar:'
                      '~/pycharm-2017.2.3/lib/util.jar:'
                      '~/pycharm-2017.2.3/lib/jdom.jar:'
                      '~/pycharm-2017.2.3/lib/log4j.jar:'
                      '~/pycharm-2017.2.3/lib/trove4j.jar:'
                      '~/pycharm-2017.2.3/lib/jna.jar -Dparser.settingsFile='
          + dirname + '/dbparser/probarser/settings/collins.properties danbikel.parser.Parser -is '
          + dirname + '/wsj-02-21/probarser/wsj-02-21.obj.gz -sa '
          + dirname + '/input/probarser/input_bikel.txt -out '
          + dirname + '/output/probarser/output_bikel.txt')
