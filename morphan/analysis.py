from . import freeling
import time
import re


def process_sentences(ls):
    # output results
    output_text = []
    start_time = time.clock()
    for s in ls:
        for w in s:
            an = w.get_analysis()
            for a in an:
                token = w.get_form()\
                        + ' ' \
                        + a.get_lemma() \
                        + ' ' \
                        + re.sub('0', '', a.get_tag())\
                        + ' '\
                        + '%.9f' % round(a.get_prob(), 9)
                if token not in output_text:
                    output_text.append(token)
            # print('PoS Tagging: (' + w.get_lemma() + ',' + w.get_tag() + ')')
    end_time = time.clock()
    print('Análisis morfológico de palabras: ' + str(end_time - start_time) + ' segundos')
    return output_text


def my_maco_options(lang, lpath):
    # create options set for maco analyzer. Default values are Ok, except for data files.
    start_time = time.clock()
    op = freeling.maco_options(lang)
    op.PunctuationFile = lpath + '../common/punct.dat'
    op.DictionaryFile = lpath + 'dicc.src'
    op.AffixFile = lpath + 'afixos.dat'
    op.LocutionsFile = lpath + 'locucions.dat'
    op.NPdataFile = lpath + 'np.dat'
    op.QuantitiesFile = lpath + 'quantities.dat'
    op.ProbabilityFile = lpath + 'probabilitats.dat'
    end_time = time.clock()
    print('Creando opciones para el analizador morfológico: ' + str(end_time - start_time) + ' segundos')
    return op


def analyze(input_text):
    start_time = time.clock()
    freeling.util_init_locale('default')
    end_time = time.clock()
    print('Init locale: ' + str(end_time - start_time) + ' segundos')
    lang = 'es'
    # Modify this line to be your FreeLing installation directory
    freeling_dir = '/usr/local'
    data = freeling_dir + '/share/freeling/' + lang + "/"
    # create analyzers
    tk = freeling.tokenizer(data + 'tokenizer.dat')
    sp = freeling.splitter(data + 'splitter.dat')

    start_time = time.clock()
    morfo = freeling.maco(my_maco_options(lang, data))
    end_time = time.clock()
    print('Creando analizador morfológico: ' + str(end_time - start_time) + ' segundos')

    # activate morpho modules to be used in next call
    morfo.set_active_options(False,  # UserMap
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
    # create tagger
    tagger = freeling.hmm_tagger(data + "tagger.dat", True, 2)
    # process input text
    lin = input_text
    start_time = time.clock()
    phrase = tk.tokenize(lin)
    ls = sp.split(phrase)
    ls = morfo.analyze(ls)
    ls = tagger.analyze(ls)
    end_time = time.clock()
    print('Analizando sentencias: ' + str(end_time - start_time) + ' segundos')
    return process_sentences(ls)
