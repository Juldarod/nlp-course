# Splits text into parts. Each part represent a single tree.
def partition(text, start_tag, end_tag):
    partitions = []
    i = 0
    level = 0
    for c in text:
        if c == start_tag:
            if level == 0:
                start = i
            level = level + 1
        if c == end_tag:
            level = level - 1
            if level == 0:
                partitions.append(text[start:(i + 1)])
        i = i + 1
    return partitions
    # Converts some nested text into tree.


def text_to_tree(text, start_tag, end_tag):
    node = ''
    children = []
    i = 0
    level = 0
    for c in text:

        if c == start_tag:
            level = level + 1

            if level == 1:
                node_start = i + 1

            if level == 2 and not node:
                node = text[node_start:i]
                child_start = i

        if c == end_tag:
            level = level - 1

            if level == 1:
                child_end = i + 1
                children.append(text_to_tree(text[child_start:child_end], start_tag, end_tag))
                child_start = i + 1

            if level == 0 and not node:
                node = text[node_start:i]

        i = i + 1
    if level != 0:
        return None  # TODO: viska hoopis erind
    return node, children


# Returns the tag form a tag-word pair
def get_tag(text):
    s = text.split()
    if s:
        return s[0].strip()
    return ''


# Returns the word form a tag-word pair
def get_word(text):
    s = text.split()
    if len(s) > 1:
        return s[1].strip()
    return ''


# Cleans a tree from specific tags tags eg. NP-SBJ and -NONE-
def clean(node):
    clean_children = []
    for child in node[1]:
        clean_child = clean(child)
        if clean_child:
            clean_children.append(clean_child)
    tag = get_tag(node[0])
    if tag == '-NONE-':
        return None
    return tag.split('-', 1)[0] + ' ' + get_word(node[0]), clean_children


# def get_sentence(node, pos=0):
#     s = str(pos) + ' '
#     if node[1]:
#         for c in node[1]:
#             s = s + ' ' + get_sentence(c, pos + 1)
#     else:
#         s = get_tag(node[0])
#     return s


# Returns a lis of tuples representing tags and their span.
# Tuples have form (tag start, tag end, tag name).
def get_segments(node, start_pos):
    segments = []

    end_pos = start_pos

    for child in node[1]:
        child_segments = get_segments(child, end_pos)
        end_pos = child_segments[len(child_segments) - 1][1] + 1
        segments.extend(child_segments)

    if node[1]:
        end_pos = end_pos - 1

    tag = get_tag(node[0])
    segments.append((start_pos, end_pos, tag))

    return segments


# Prints a list to screen
def print_list(l):
    for l in l:
        print(l)


# Prints disagreements to screen
def print_disagreements(disagreements):
    for d in disagreements:
        if d[1]:
            strings = []
            for s in d[1]:
                strings.append(str(s[2]))
            print(str(d[0][2]) + ' <==> ' + ' & '.join(strings))
        else:
            print(str(d[0][2]) + ' <==> ?')


# Checks if two segments are equal
def equal(segment1, segment2):
    if segment1[0] == segment2[0] and segment1[1] == segment2[1] and segment1[2] == segment2[2]:
        return True
    return False


# Checks if two segments cover the same words
def equal_span(segment1, segment2):
    if segment1[0] == segment2[0] and segment1[1] == segment2[1]:
        return True
    return False


# Evaluates segments1 based on segments2
def evaluate(segments1, segments2):
    correct = 0
    crossings = 0
    errors = []
    for s2 in segments2:
        for s1 in segments1:
            if equal(s1, s2):
                correct = correct + 1
                break
    precision = float(correct) / len(segments1)
    recall = float(correct) / len(segments2)

    # Find errors
    for s1 in segments1:
        candidates = []
        found = False
        found_crossing = False
        for s2 in segments2:
            if equal(s1, s2):
                found = True
                break
            elif equal_span(s1, s2):
                candidates.append(s2)
            # Check cross-brackets
            if (s1[0] < s2[0] and (s2[0] < s1[1] < s2[1])) or (
                    (s2[0] < s1[0] and (s1[0] < s2[1] < s1[1]))):
                found_crossing = True
        if not found:
            errors.append((s1, candidates))
        if found_crossing:
            crossings = crossings + 1

        crossing = float(crossings) / len(segments1)

    return precision, recall, crossing, errors


# Returns a list of text-tree-segments tuples taken from a file
# def process(file_name, to_clean=False):
#     data = []
#
#     file = open(file_name, 'r')
#     text = file.read()
#     file.close()
#
#     parts = partition(text, start_tag, end_tag)
#     for part in parts:
#         tree = text_to_tree(part, start_tag, end_tag)
#         if to_clean:
#             tree = to_clean(tree)
#         segments = get_segments(tree, 1)
#         data.append([part, tree, segments])
#
#     return data
