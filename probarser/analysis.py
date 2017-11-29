import time
from morphan.freeling.morphan import freeling


def my_maco_options(lang, lang_path):
    # Create options set for maco analyzer. Default values are OK, except for data files.
    options = freeling.maco_options(lang)
    options.PunctuationFile = lang_path + '../common/punct.dat'
    options.DictionaryFile = lang_path + 'dicc.src'
    options.AffixFile = lang_path + 'afixos.dat'
    options.LocutionsFile = lang_path + 'locucions.dat'
    options.NPdataFile = lang_path + 'np.dat'
    options.QuantitiesFile = lang_path + 'quantities.dat'
    options.ProbabilityFile = lang_path + 'probabilitats.dat'
    return options


def pos_tag_sentences(ls):
    # Output results
    output = ''
    start_time = time.clock()
    for s in ls:
        sentence = ''
        for w in s:
            if w.get_tag() == 'Fp':
                sentence = sentence + '(' + w.get_form() + ' (.)) '
            else:
                sentence = sentence + '(' + w.get_form() + ' (' + w.get_tag() + ')) '
        output = output + '(' + sentence[:-1] + ') '
    end_time = time.clock()
    print(output)
    print('PoS Tagging: ' + '%.6f' % round(end_time - start_time, 6) + ' seconds\n')
    return output


class Analysis(object):
    def __init__(self):
        freeling.util_init_locale('default')
        lang = 'en'
        # Modify this line to be your FreeLing installation directory
        freeling_dir = '/usr/local'
        data = freeling_dir + '/share/freeling/' + lang + "/"
        # Create analyzers
        self.tk = freeling.tokenizer(data + 'tokenizer.dat')
        self.sp = freeling.splitter(data + 'splitter.dat')
        start_time = time.clock()
        self.morpho = freeling.maco(my_maco_options(lang, data))
        end_time = time.clock()
        print('Creating English analyzer: ' + '%.6f' % round(end_time - start_time, 6) + ' seconds\n')
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
        # Create tagger
        self.tagger = freeling.hmm_tagger(data + "tagger.dat", True, 2)

    def pos_tagging(self, input_text):
        # Process input text
        start_time = time.clock()
        phrase = self.tk.tokenize(input_text)
        ls = self.sp.split(phrase)
        ls = self.morpho.analyze(ls)
        ls = self.tagger.analyze(ls)
        end_time = time.clock()
        print('Analyzing sentences: ' + '%.6f' % round(end_time - start_time, 6) + ' seconds\n')
        return pos_tag_sentences(ls)
