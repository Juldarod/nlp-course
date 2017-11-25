#!/usr/bin/env python

# import getopt
# import os
# import re
# import shlex
# import subprocess
import sys
# from subprocess import Popen, PIPE
#
# import nltk
# import per1
# from NLPlib import *
from per1 import partition, text_to_tree, clean, get_segments, evaluate, print_list, print_disagreements


# nlp = NLPlib()


def parseval(files1, files2, argv):
    # Execution start here ##########

    start_tag = '('
    end_tag = ')'

    do_cleanup = False
    show_trees = False
    show_segments = False
    show_individual_eval = False
    show_disagreements = False
    file_names = []
    # data = []  # A List for holding trees and segments
    # Check command line arguments
    # print argv
    for o in argv:
        if o == '-c':
            do_cleanup = True
        elif o == '-s':
            show_segments = True
        elif o == '-t':
            show_trees = True
        elif o == '-i':
            show_individual_eval = True
        elif o == '-d':
            show_disagreements = True
        else:
            file_names.append(o)

    # Check if there were enough arguments
    if len(files1) < 1 and len(files2) < 1:
        # Print out some information
        print('usage: parseval [file 1] [file 2] [options]')
        print('example: parseval parse.txt gold.txt -c')
        print('Precision, recall and cross-bracketing are given in tuples (prescision, recall, cross bracketing).')
        print('-c    remove unidentified words and additional labels eg. NP-SBJ --> NP')
        print('-s    display tags and their span')
        print('-t    display trees')
        print('-i    show evaluation results for every single tree')
        print('-d    show errors, prints "?" where constituent spans do not match')
        sys.exit()

    # print 'entro aqui', files1,len(files1)
    # Process the first file

    try:
        file1 = open(files1, 'r')
        text1 = file1.read()
        file1.close()
    except:
        print('Invalid file.')
        sys.exit()

    trees1 = []
    segments1 = []
    parts1 = partition(text1, start_tag, end_tag)
    for part in parts1:
        tree = text_to_tree(part, start_tag, end_tag)
        if do_cleanup:
            tree = clean(tree)
        trees1.append(tree)
        segments1.append(get_segments(tree, 1))

        # Process the second file
    try:
        file2 = open(files2, 'r')
        text2 = file2.read()
        file2.close()
    except:
        print('Invalid file.')
        sys.exit()

    trees2 = []
    segments2 = []
    parts2 = partition(text2, start_tag, end_tag)
    for part in parts2:
        tree = text_to_tree(part, start_tag, end_tag)
        if do_cleanup:
            tree = clean(tree)
        trees2.append(tree)
        segments2.append(get_segments(tree, 1))
        # print parts1

        # Evaluate and print the output
    print('')
    precision = recall = crossing = 0
    for i in range(len(parts1)):
        if show_trees or show_segments or show_individual_eval or show_disagreements:
            print('########## ' + str(i) + ' ##########')
            print('')
        if show_trees:
            print(parts1[i])
            print('')
            print(parts2[i])
            print('')
        if show_segments:
            print_list(segments1[i])
            print('')
            print_list(segments2[i])
            print('')
        to_eval = evaluate(segments1[i], segments2[i])
        if show_individual_eval:
            print(to_eval[:3])
            print('')
        if show_disagreements:
            print_disagreements(to_eval[3])
            print('')
            # print 'ESTA EL ERROR'
        precision = precision + to_eval[0]
        recall = recall + to_eval[1]
        crossing = crossing + to_eval[2]
    # LP es la precision que es el numero de constituyentes correctos in el analizador
    # propuesto sobre el numero de constituyentes en el analizador propuesto
    # LR es el recall que es el numero correcto de constituyentes en el analizador
    # propuesto sobre el numero de constituyentes en el treebank parse
    # print parts1
    precision = precision / len(parts1)
    recall = recall / len(parts2)
    crossing = crossing / len(parts1)
    pre1 = precision * 100
    re1 = recall * 100
    fscore = (2 * pre1 * re1) / (pre1 + re1)
    # fscore es la media armonica entre LP y LR

    print('########## TOTAL ##########')
    print('')
    print('Average precision, recall,  cross brackets and F-score:')
    print(pre1, re1, crossing, fscore)


# class Modelo(object):
#     def __init__(self):
#         self.pareja = []
#         self.lista = []
#
#     def ejecute(self):
#         global pareja1
#         # base_path = os.getcwd() + '/' + sys.argv[1]
#         # pathname='/media/raul/datos/test-argumentos'
#         pathname = '/home/raul/tages'
#         # print pathname
#         base_path = pathname + '/' + sys.argv[1]
#         # print base_path
#
#         os.system("perl splitter.pl -f " + base_path + " -o")
#         base = pathname + '/' + sys.argv[1]
#         f5 = open(base_path, 'ru')  # Esta es una forma sencilla que lee del archivo raw
#         # f = open('/media/raul/datos/tageador1/salida.split', 'rU')
#         # esta posibilidad es utilizando el spliteador de Clough
#         f = open('/home/raul/tages/salida.split', 'rU')
#         # f1= open('/media/raul/datos/tageador1/salida.dbp.in', 'w')
#         f1 = open('/home/raul/tages/salida.dbp.in', 'w')
#         pareja1 = []
#         for line in f:
#             print(line)
#             line = line.strip()
#             # print line.strip()
#             tokens = nlp.tokenize(line)
#             tagged = nlp.tag(tokens)
#             i = 0
#             while i < len(tokens):
#                 if tokens[i] != " " and tagged[i] != " ":
#                     pareja1.append("(" + tokens[i] + " " + "(" + tagged[i] + ")" + ")")
#                     print("(", tokens[i], "(", tagged[i], ")", ")")
#                 i += 1
#
#         print('esta es el arreglo guardado')
#         f1.write("(")
#         for parejita in pareja1:
#             # print parejita
#             if parejita != "(. (.))":
#                 f1.write(str(parejita))
#                 # print parejita
#             else:
#                 f1.write(str(parejita + ")"))
#                 f1.write(str("("))
#         f.close()
#         f1.close()
#
#     def entrenar(self):
#         os.system("java -server -Xms800m -Xmx800m -cp /home/raul/dbparser/dbparser.jar "
#                   "-Dparser.settingsFile=/media/raul/datos/dbparser/settings/arabic.properties "
#                   "danbikel.parser.Trainer -i /home/raul/tages/wsj-02-21.mrg -o "
#                   "/home/raul/tages/wsj-02-21.observed.gz -od /home/raul/tages/wsj-02-21.obj.gz")
#
#     def testear(self):
#         os.system("java -server -Xms500m -Xmx500m -cp /home/raul/dbparser/dbparser.jar "
#                   "-Dparser.settingsFile=/home/raul/dbparser/settings/arabic.properties danbikel.parser.Parser "
#                   "-is /home/raul/tages/wsj-02-21.obj.gz -sa /home/raul/tages/salida.dbp.in")
#
#     def tageador(self):
#         self.ejecute()
#         self.entrenar()
#         self.testear()


if __name__ == "__main__":
    # model = Modelo()
    # l = sys.argv[1]
    # model.ejecute()
    # model.tageador()
    # model.ejecute()
    # model.entrenar()
    # model.testear()
    input1 = '/home/juldini/Downloads/parseval/siembra'
    input2 = '/home/juldini/Downloads/parseval/wsj_0001.mrg'
    parseval(input1, input2, ['-i', '-s'])
