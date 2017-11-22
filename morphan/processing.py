from morphan.analysis import analyze
from morphan.segmentation import segment
from morphan.dictionary import make_dictionary
from nltk.tokenize import TweetTokenizer


class Processing:
    emoticon = []
    money = []
    comma = []
    mayor = []

    @staticmethod
    def get_dictionary():
        return make_dictionary()

    @staticmethod
    def nltk_tweet_tokenizer(phrase):
        tokenizer = TweetTokenizer()
        print('\nNLTK TweetTokenizer\n' + str(tokenizer.tokenize(phrase)) + '\n')
        return tokenizer.tokenize(phrase)

    @staticmethod
    def my_tokenizer(tokenized_text, corpus):
        new_tokenized_text = []
        for token in tokenized_text:
            if '#' in token or '@' in token:
                print('Segmentando hashtag/nickname... ' + token)
                segmented_token = segment(token, corpus)
                print(segmented_token)
                len_segmented_token = len(segmented_token)
                for i in range(len_segmented_token):
                    new_tokenized_text.append(segmented_token[i])
            else:
                new_tokenized_text.append(token)
        print('\nTokenización con hashtags/nicknames \n' + str(new_tokenized_text) + '\n')
        return new_tokenized_text

    def get_raw_text(self, new_tokenized_text):
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
                self.emoticon.append([new_tokenized_text.index(token), token, 'E'])
            elif token in m:
                self.money.append([new_tokenized_text.index(token), token, '$'])
            elif token in c:
                self.comma.append([new_tokenized_text.index(token), token, ','])
            elif token in g:
                self.mayor.append([new_tokenized_text.index(token), token, 'G'])
            else:
                # if token not in tokens:
                tokens.append(token)
        for token in tokens:
            raw_text += token + ' '
        return raw_text.strip()

    @staticmethod
    def analyze_raw_text(raw_text):
        return analyze(raw_text)

    def make_text(self, analyzed_words, new_tokenized_text):
        print(analyzed_words)
        text = []
        emoticon = self.emoticon
        money = self.money
        comma = self.comma
        mayor = self.mayor
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
                        # print('')
                        text.append(word.split(' '))
        emoticon.clear()
        money.clear()
        comma.clear()
        mayor.clear()
        return text
