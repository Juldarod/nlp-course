import time
import re
from morphan.freeling.morphan import freeling


def my_maco_options(lang, lang_path):
    # Create options set for maco analyzer. Default values are OK, except for data files.
    # start_time = time.clock()
    options = freeling.maco_options(lang)
    options.PunctuationFile = lang_path + '../common/punct.dat'
    options.DictionaryFile = lang_path + 'dicc.src'
    options.AffixFile = lang_path + 'afixos.dat'
    options.LocutionsFile = lang_path + 'locucions.dat'
    options.NPdataFile = lang_path + 'np.dat'
    options.QuantitiesFile = lang_path + 'quantities.dat'
    options.ProbabilityFile = lang_path + 'probabilitats.dat'
    # end_time = time.clock()
    # print('Setting options for morphological analysis: ' + '%.6f' % round(end_time - start_time, 6) + ' seconds')
    return options


def process_sentences(ls):
    # Output results
    output_text = []
    start_time = time.clock()
    for s in ls:
        for w in s:
            an = w.get_analysis()
            for a in an:
                token = w.get_form() \
                        + ' ' \
                        + a.get_lemma() \
                        + ' ' \
                        + re.sub('0', '', a.get_tag()) \
                        + ' ' \
                        + '%.9f' % round(a.get_prob(), 9)
                if token not in output_text:
                    output_text.append(token)
    end_time = time.clock()
    print('Morphological analysis: ' + '%.6f' % round(end_time - start_time, 6) + ' seconds\n')
    return output_text


class Analysis(object):
    def __init__(self):
        # start_time = time.clock()
        freeling.util_init_locale('default')
        # end_time = time.clock()
        # print('Init locale: ' + '%.6f' % round(end_time - start_time, 6) + ' seconds')
        lang = 'es'
        # Modify this line to be your FreeLing installation directory
        freeling_dir = '/usr/local'
        data = freeling_dir + '/share/freeling/' + lang + "/"
        # Create analyzers
        self.tk = freeling.tokenizer(data + 'tokenizer.dat')
        self.sp = freeling.splitter(data + 'splitter.dat')
        start_time = time.clock()
        self.morpho = freeling.maco(my_maco_options(lang, data))
        end_time = time.clock()
        print('Creating Spanish analyzer: ' + '%.6f' % round(end_time - start_time, 6) + ' seconds')
        # Activate morpho modules to be used in next call
        self.morpho.set_active_options(False,  # UserMap
                                       True,  # NumbersDetection,
                                       True,  # PunctuationDetection,
                                       True,  # DatesDetection,
                                       True,  # DictionarySearch,
                                       True,  # AffixAnalysis,
                                       False,  # CompoundAnalysis,
                                       True,  # RetokContractions,
                                       True,  # MultiwordsDetection,
                                       False,  # NERecognition,
                                       True,  # QuantitiesDetection,
                                       True)  # ProbabilityAssignment

    def analyze(self, input_text):
        # Process input text
        start_time = time.clock()
        phrase = self.tk.tokenize(input_text)
        ls = self.sp.split(phrase)
        ls = self.morpho.analyze(ls)
        end_time = time.clock()
        print('Analyzing sentences: ' + '%.6f' % round(end_time - start_time, 6) + ' seconds\n')
        return process_sentences(ls)
