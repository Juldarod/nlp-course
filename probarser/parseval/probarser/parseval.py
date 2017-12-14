import sys
from probarser.parseval.probarser.per1 import *


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

        precision = precision + to_eval[0]
        recall = recall + to_eval[1]
        crossing = crossing + to_eval[2]

    # LP es la precisión, que es el número de constituyentes correctos en el analizador
    # propuesto sobre el número de constituyentes en el analizador propuesto.
    # LR es el recall, que es el número correcto de constituyentes en el analizador
    # propuesto sobre el número de constituyentes en el treebank parse.

    precision = precision / len(parts1)
    recall = recall / len(parts2)
    # crossing = crossing / len(parts1)
    pre1 = precision * 100
    re1 = recall * 100
    fscore = (2 * pre1 * re1) / (pre1 + re1)
    # fscore es la media armónica entre LP y LR.

    # print('########## TOTAL ##########')
    # print('')
    # print('Average precision, recall, and F-score:')
    # print(pre1, re1, fscore)
    return [pre1, re1, fscore]


# input1 = '/home/juldini/PycharmProjects/nlp-course/tests-parseval/wsj_00010.st'
# input1 = '/home/juldini/PycharmProjects/nlp-course/tests-parseval/wsj_0001.bk'
# input2 = '/home/juldini/PycharmProjects/nlp-course/tests-parseval/wsj_00010.mrg'
# parseval(input1, input2, ['-i', '-s'])
#
# for i in range(1, 11):
#     parseval('/home/juldini/PycharmProjects/nlp-course/tests-parseval/wsj_000%s.st' % i,
#              '/home/juldini/PycharmProjects/nlp-course/tests-parseval/wsj_000%s.mrg' % i,
#              [])
#
# for i in range(1, 11):
#     parseval('/home/juldini/PycharmProjects/nlp-course/tests-parseval/wsj_000%s.bk' % i,
#              '/home/juldini/PycharmProjects/nlp-course/tests-parseval/wsj_000%s.mrg' % i,
#              [])
