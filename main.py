import datetime
import file_reader as fr
import pre_processor as ps
from nltk import sent_tokenize


# process starts
start_time = datetime.datetime.now()

# get text files (text level)
files = []
files = fr.get_files('data\\')
print('\n' + 'Total number of ' + str(len(files)) + ' files need(s) to be processed')

# get contents
documents = []
for f in files:
    with open(f, 'r') as file:
        documents.append(file.read())

# get word count
num_words = 0
for idx, d in enumerate(documents):
    words = documents[idx].split()
    num_words += len(words)
print('Total number of words: ' + str(num_words))

# get sentence count
num_sentences = 0
for idx, d in enumerate(documents):
    sentences = sent_tokenize(documents[idx])
    num_sentences += len(sentences)
print('Total number of sentences: ' + str(num_sentences))


# pre-process step 01: fix contradictions
for idx, d in enumerate(documents):
    documents[idx] = ps.fix_contractions(d)

# pre-process step 02: tokenize documents
tok_documents = []
for idx, d in enumerate(documents):
    tok_documents.append(ps.tokenize(d))

# pre-process step 03: remove non ascii characters
for idx, d in enumerate(tok_documents):
    tok_documents[idx] = ps.remove_non_ascii_chars(d)

# pre-process step 04: convert characters into lower cases
for idx, d in enumerate(tok_documents):
    tok_documents[idx] = ps.convert_to_lower(d)

# pre-process step 05: remove punctuations
for idx, d in enumerate(tok_documents):
    tok_documents[idx] = ps.remove_punctuations(d)

# pre-process step 06: convert int to string representation
for idx, d in enumerate(tok_documents):
    tok_documents[idx] = ps.convert_number_to_words(d)

# pre-process step 07: remove stop words
for idx, d in enumerate(tok_documents):
    tok_documents[idx] = ps.remove_stop_words(d)

# pre-process step 08: part of speech tagging
for idx, d in enumerate(tok_documents):
    tok_documents[idx] = ps.pos_tag(d)

# pre-process step 09: chunking
for idx, d in enumerate(tok_documents):
    tok_documents[idx] = ps.chunk_sentence(d)

# this part is not working well
# pre-process step 10: named entity recognition
for idx, d in enumerate(documents):
    documents[idx] = ps.ner_tag(d)


# stemming, lemmatization should be performed if required
# https://medium.com/@datamonsters/text-preprocessing-in-python-steps-tools-and-examples-bf025f872908


# process ends
end_time = datetime.datetime.now()
print('\nProcess start  time: ' + str(start_time))
print('Process finish time: ' + str(end_time))
