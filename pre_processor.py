import re
import nltk
import unicodedata
import contractions


def tokenize(text):
    return nltk.word_tokenize(text)


def convert_to_lower(words):
    word_list = []
    for w in words:
        word = w.lower()
        word_list.append(word)
    return word_list


def fix_contractions(text):
    return contractions.fix(text)


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
        word = unicodedata.normalize('NFKD', w).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        word_list.append(word)
    return word_list
