from nltk.parse.stanford import StanfordParser
from nltk.tree import Tree


model = "/usr/share/stanford-parser/englishPCFG.ser.gz"
jar = "/usr/share/stanford-parser/stanford-parser.jar"

parser = StanfordParser(model, jar)
raw_tree = parser.raw_parse("My dog also likes eating sausage.")
# raw_sents_tree = parser.raw_parse_sents(["My dog also likes eating sausage.", "I do too."])


def list_to_tree(old_tree):
    tree = object
    for t in old_tree:
        tree = Tree(t.label(), t)
    return tree[0]


new_tree = list_to_tree(raw_tree)

print(type(new_tree))
print(new_tree)
print('')

# for t in raw_sents_tree:
#     for s in t:
#         print(s[0])
# print('')

bikel_tree = Tree.fromstring("(S (NP (PRP$ My) (NN dog)) (ADVP (RB also)) (VP (VBZ likes) (VP (VBG eating) (NP "
                             "(NN sausage)))) (. .))")
print(type(bikel_tree))
print(bikel_tree)
print('')

print(' '.join(str(new_tree).split()))
print(' '.join(str(bikel_tree).split()))

