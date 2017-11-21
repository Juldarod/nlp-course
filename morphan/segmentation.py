def greedy_search(input_phrase, corpus):
    current_token = ''
    for i in range(len(input_phrase) + 1):
        if input_phrase[:i] in corpus:
            current_token = input_phrase[:i]
    return current_token


def reverse_search(input_phrase, corpus):
    current_token = ''
    for i in range(len(input_phrase) + 1):
        if input_phrase[len(input_phrase) - i:] in corpus:
            current_token = input_phrase[len(input_phrase) - i:]
    return current_token


def greedy_max_match(input_phrase, corpus):
    segments = []
    while input_phrase != '':
        len_input = len(input_phrase) + 1
        token = greedy_search(input_phrase, corpus)
        if '' == token:
            segments.append(['not found', input_phrase[:1]])
            input_phrase = input_phrase[1:]
        elif input_phrase == token:
            segments.append(['found', token])
            input_phrase = input_phrase[:-len_input + len(token) + 1]
        else:
            segments.append(['found', token])
            input_phrase = input_phrase[-len_input + len(token) + 1:]
    return segments


def reverse_max_match(input_phrase, corpus):
    segments = []
    while input_phrase != '':
        len_input = len(input_phrase) + 1
        token = reverse_search(input_phrase, corpus)
        if '' == token:
            segments.append(['not found', input_phrase[-1:]])
            input_phrase = input_phrase[:-1]
        else:
            segments.append(['found', token])
            input_phrase = input_phrase[:len_input - 1 - len(token)]
    return segments


def process_greedy_tokens(greedy_tokens):
    found = 0
    not_found = 0
    tokenized_text = ''
    for pos in greedy_tokens:
        if pos[0] == 'found':
            found += 1
            tokenized_text += ' ' + pos[1] + ' '
        else:
            not_found += 1
            tokenized_text += pos[1]
    return [found, not_found, tokenized_text.strip().split()]


def process_reverse_tokens(reverse_tokens):
    found = 0
    not_found = 0
    tokenized_text = ''
    for pos in reverse_tokens:
        if pos[0] == 'found':
            found += 1
            tokenized_text = ' ' + pos[1] + ' ' + tokenized_text
        else:
            not_found += 1
            tokenized_text = pos[1] + tokenized_text
    return [found, not_found, tokenized_text.strip().split()]


def segment(input_phrase, corpus):
    if input_phrase[:1] == '#':
        actual_phrase = input_phrase.split('#')
    else:
        actual_phrase = input_phrase.split('@')
    actual_phrase = actual_phrase[1]
    actual_phrase = actual_phrase.lower()
    greedy_tokens = greedy_max_match(actual_phrase, corpus)
    reverse_tokens = reverse_max_match(actual_phrase, corpus)
    processed_greedy_tokens = process_greedy_tokens(greedy_tokens)
    processed_reverse_tokens = process_reverse_tokens(reverse_tokens)
    if processed_greedy_tokens[0] >= processed_reverse_tokens[0]:
        if processed_greedy_tokens[1] < processed_reverse_tokens[1]:
            print('Greedy')
            return processed_greedy_tokens[2]
        else:
            print('Reverse')
            return processed_reverse_tokens[2]
    else:
        print('Reverse')
        return processed_reverse_tokens[2]
