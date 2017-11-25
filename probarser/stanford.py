from nltk.parse.stanford import StanfordParser
from nltk.tree import Tree


model = '/usr/share/stanford-parser/englishPCFG.ser.gz'
jar = '/usr/share/stanford-parser/stanford-parser.jar'

parser = StanfordParser(model, jar)
raw_tree = parser.raw_parse('Tokyo Ghoul is set in an alternate reality where ghouls, individuals who can only '
                            'survive by eating human flesh, live among the normal humans in secret, hiding their true '
                            'nature to evade pursuit from the authorities.')
# raw_sents_tree = parser.raw_parse_sents(["My dog also likes eating sausage.", "I do too."])


def list_to_tree(old_tree):
    tree = object
    for t in old_tree:
        tree = Tree(t.label(), t)
    return tree[0]


stanford_tree = list_to_tree(raw_tree)

print(type(stanford_tree))
print(stanford_tree)
print('')

# for t in raw_sents_tree:
#     for s in t:
#         print(s[0])
# print('')

bikel_tree = Tree.fromstring('(S (NP (NNP Tokyo) (NN Ghoul)) (VP (VBZ is) (VP (VBN set) (PP (IN in) (NP (NP (DT an) ('
                             'JJ alternate) (NN reality)) (SBAR (WHADVP (WRB where)) (S (NP (NP (NNS ghouls)) (, ,'
                             ') (NP (NP (NNS individuals)) (SBAR (WHNP (WP who)) (S (VP (MD can) (ADVP (RB only)) (VP '
                             '(VB survive) (PP (IN by) (S (VP (VBG eating) (NP (JJ human) (NN flesh))))))))))) (, ,'
                             ') (VP (VBP live) (PP (IN among) (NP (DT the) (JJ normal) (NNS humans))) (PP (IN in) ('
                             'ADJP (JJ secret))) (, ,) (S (VP (VBG hiding) (NP (PRP$ their) (JJ true) (NN nature)) (S '
                             '(VP (TO to) (VP (VB evade) (NP (NN pursuit)) (PP (IN from) (NP (DT the) (NNS '
                             'authorities))))))))))))))) (. .))')
print(type(bikel_tree))
print(bikel_tree)
print('')

print(' '.join(str(stanford_tree).split()))
print(' '.join(str(bikel_tree).split()))

