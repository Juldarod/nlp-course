import probarser.stanford
from probarser.bikel import *


def process_to_stanford(input_text):
    return probarser.stanford.parse(input_text)


def process_to_bikel(input_text):
    return ''


class Processing(object):
    def __init__(self, input_text, analyzer):
        self.input_text = analyzer.pos_tagging(input_text)

    def process(self, input_text):
        stanford = process_to_stanford(input_text)
        bikel = process_to_bikel(self.input_text)
        return [stanford, bikel]
