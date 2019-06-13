import nltk
import spacy
import datetime
import en_core_web_sm
import file_reader as fr
import pre_processor as ps
from pprint import pprint
from spacy import displacy
from nltk import sent_tokenize
from collections import Counter
from sacremoses import MosesDetokenizer

# process starts
start_time = datetime.datetime.now()
nlp = en_core_web_sm.load()

# read all text files from the data folder
files = []
files = fr.get_files('data\\')
print('\n' + 'Total number of ' + str(len(files)) + ' files need(s) to be processed')

# get all contents from the text files
documents = []
for f in files:
    with open(f, 'r') as file:
        documents.append(file.read())

# get word count
num_words = 0
for idx, d in enumerate(documents):
    word_list = documents[idx].split()
    num_words += len(word_list)
print('Total number of words: ' + str(num_words))

# get sentence count
num_sentences = 0
for idx, d in enumerate(documents):
    sentence_list = sent_tokenize(documents[idx])
    num_sentences += len(sentence_list)
print('Total number of sentences: ' + str(num_sentences))

mod_documents = []

# pre-process step 01: fix contradictions
for idx, d in enumerate(documents):
    # tok_documents[idx] = ps.fix_contractions(d)
    mod_documents.append(ps.fix_contractions(d))
# print(mod_documents)

# # pre-process step 02: tokenize documents
# tok_documents = []
# for idx, d in enumerate(documents):
#     tok_documents.append(ps.tokenize(d))

# pre-process step 03: remove non ascii characters
for idx, d in enumerate(mod_documents):
    mod_documents[idx] = ps.remove_non_ascii_chars(d)
# print(mod_documents)

# # pre-process step 04: convert characters into lower cases
# for idx, d in enumerate(mod_documents):
#     mod_documents[idx] = ps.convert_to_lower(d)
# # print(mod_documents)

# pre-process step 05: remove punctuations
for idx, d in enumerate(mod_documents):
    mod_documents[idx] = ps.remove_punctuations(d)
# print(mod_documents)

# pre-process step 06: convert int to string representation
for idx, d in enumerate(mod_documents):
    mod_documents[idx] = ps.convert_number_to_words(d)
# print(mod_documents)

# pre-process step 07: remove stop words
for idx, d in enumerate(mod_documents):
    mod_documents[idx] = ps.remove_stop_words(d)
# print(mod_documents)

# # pre-process step 08: part of speech tagging
# for idx, d in enumerate(tok_documents):
#     tok_documents[idx] = ps.pos_tag(d)

# # pre-process step 09: chunking
# for idx, d in enumerate(tok_documents):
#     tok_documents[idx] = ps.chunk_sentence(d)

# detokenize before process ner, which need to be tokenized again (not working well)
detokenizer = MosesDetokenizer(lang='en')

word_bag = []
for idx, d in enumerate(mod_documents):
    word_list = mod_documents[idx]
    word_bag += word_list

# pre-process step 10: named entity recognition
temp_documents = []
temp_documents.append(ps.apply_ner(detokenizer.detokenize(word_bag)))
# print(temp_documents)

# collect nouns
# noun_bag = []
# noun_bag = nltk.FreqDist(word for (word, tag) in temp_documents[0] if tag == 'NN')
# print(noun_bag.most_common())

# stemming, lemmatization should be performed if required
# https://medium.com/@datamonsters/text-preprocessing-in-python-steps-tools-and-examples-bf025f872908

# spacy ner
doc = []
for x in range(3):
    doc.append(nlp(detokenizer.detokenize(word_bag[int(len(word_bag) / 3 * x):int((len(word_bag) / 3 * (x + 1)))])))

for x in range(3):
    print('Total number of entities for batch ' + str(x + 1) + ': ' + str(len(doc[x])))

# label summary
for i in range(3):
    labels = [x.label_ for x in doc[i].ents]
    print('\nEntity summary for batch ' + str(i + 1) + ':')
    pprint(Counter(labels))

# most common items
# items = [x.text for x in doc.ents]
# pprint(Counter(items).most_common(3))

# most common organizations
target_orgs = []
for i in range(3):
    organizations = [x.text for x in doc[i].ents if x.label_ == 'ORG']
    target_orgs.append(Counter(organizations).most_common(5))

for i in range(3):
    print('\nTop 5 most commonly appeared organizations for batch ' + str(i + 1) + ':')
    pprint(target_orgs[i])

# get articles which contain the target words
for i in range(3):
    target_orgs[i] = [org for (org, count) in target_orgs[i]]

for i in range(3):
    for didx, d in enumerate(documents):
        for oidx, o in enumerate(target_orgs[i]):
            if o in d:
                file = open('./output/' + str(o) + '.txt', 'a+')
                file.writelines(d)
                file.close()

# process ends
end_time = datetime.datetime.now()
print('\nProcess start  time: ' + str(start_time))
print('Process finish time: ' + str(end_time))
