import time
from morphan.segmentation import segment
from morphan.dictionary import make_dictionary
from nltk.tokenize import TweetTokenizer


def make_text(analyzed_words, new_tokenized_text, emoticon, money, comma, mayor):
    print(analyzed_words)
    text = []
    len_emoticon = len(emoticon)
    len_money = len(money)
    len_comma = len(comma)
    len_mayor = len(mayor)
    cont_emoticon = 0
    cont_money = 0
    cont_comma = 0
    cont_mayor = 0
    for token in new_tokenized_text:
        if len_emoticon != 0 and token == emoticon[cont_emoticon][1]:
            text.append([emoticon[cont_emoticon][1], '', emoticon[cont_emoticon][2], ''])
            cont_emoticon += 1
            len_emoticon -= 1
        elif len_money != 0 and token == money[cont_money][1]:
            text.append([money[cont_money][1], '', money[cont_money][2], ''])
            cont_money += 1
            len_money -= 1
        elif len_comma != 0 and token == comma[cont_comma][1]:
            text.append([comma[cont_comma][1], '', comma[cont_comma][2], ''])
            cont_comma += 1
            len_comma -= 1
        elif len_mayor != 0 and token == mayor[cont_mayor][1]:
            text.append([mayor[cont_mayor][1], '', mayor[cont_mayor][2], ''])
            cont_mayor += 1
            len_mayor -= 1
        else:
            for word in analyzed_words:
                if token == word.split(' ')[0]:
                    text.append(word.split(' '))
    return text


def get_raw_text(new_tokenized_text, emoticon, money, comma, mayor):
    tokens = []
    raw_text = ''
    e = [':o', ':/', ':\'(', '>:o', '(:', ':)', '>.<', 'XD',
         '-__-', 'o.O', ';D', ':-)', '@_@', ':P', '8D',
         '>:(', ':D', '=|']
    m = ['1']
    c = ['\"', ')', ':']
    g = ['>']
    for token in new_tokenized_text:
        if token in e:
            emoticon.append([new_tokenized_text.index(token), token, 'E'])
        elif token in m:
            money.append([new_tokenized_text.index(token), token, '$'])
        elif token in c:
            comma.append([new_tokenized_text.index(token), token, ','])
        elif token in g:
            mayor.append([new_tokenized_text.index(token), token, 'G'])
        else:
            # if token not in tokens:
            tokens.append(token)
    for token in tokens:
        raw_text += token + ' '
    return raw_text.strip()


def segment_hashtag(tokenized_text, corpus):
    new_tokenized_text = []
    for token in tokenized_text:
        if '#' in token or '@' in token:
            print('Segmenting hashtag/nickname... ' + token)
            start_time = time.clock()
            segmented_token = segment(token, corpus)
            end_time = time.clock()
            print(segmented_token)
            print('Segmented in: ' + '%.6f' % round(end_time - start_time, 6) + ' seconds\n')
            len_segmented_token = len(segmented_token)
            for i in range(len_segmented_token):
                new_tokenized_text.append(segmented_token[i])
        else:
            new_tokenized_text.append(token)
    print('\nTokenization with hashtags/nicknames \n' + str(new_tokenized_text) + '\n')
    return new_tokenized_text


def nltk_tweet_tokenizer(phrase):
    tokenizer = TweetTokenizer()
    print('\nNLTK TweetTokenizer\n' + str(tokenizer.tokenize(phrase)) + '\n')
    return tokenizer.tokenize(phrase)


def dictionary():
    return make_dictionary()


class Processing(object):
    def __init__(self, emoticon, money, comma, mayor):
        self.emoticon = emoticon
        self.money = money
        self.comma = comma
        self.mayor = mayor

    def process(self, corpus, input_text, analyser):
        tokenized_text = nltk_tweet_tokenizer(input_text)
        new_tokenized_text = segment_hashtag(tokenized_text, corpus)
        raw_text = get_raw_text(new_tokenized_text, self.emoticon, self.money, self.comma, self.mayor)
        analyzed_words = analyser.analyze(raw_text + '.')
        return make_text(analyzed_words, new_tokenized_text, self.emoticon, self.money, self.comma, self.mayor)
