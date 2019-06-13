import re
import nltk
import inflect
import unicodedata
import contractions
from nltk.corpus import stopwords


def tokenize(text):
    return nltk.word_tokenize(text)


def fix_contractions(text):
    return contractions.fix(text)


def convert_to_lower(words):
    word_list = []
    for w in words:
        word = w.lower()
        word_list.append(word)
    return word_list


def convert_number_to_words(words):
    processor = inflect.engine()
    word_list = []
    for w in words:
        if w.isdigit():
            word = processor.number_to_words(w)
            word_list.append(word)
        else:
            word_list.append(w)
    return word_list


def remove_stop_words(words):
    word_list = []
    for w in words:
        if w not in stopwords.words('english'):
            word_list.append(w)
    return word_list


def remove_punctuations(words):
    word_list = []
    for w in words:
        word = re.sub(r'[^\w\s]', '', w)
        if word != '':
            word_list.append(word)
    return word_list


def remove_non_ascii_chars(words):
    word_list = []
    for w in words:
        word = unicodedata.normalize('NFKD', w) \
            .encode('ascii', 'ignore')\
            .decode('utf-8', 'ignore')
        word_list.append(word)
    return word_list
