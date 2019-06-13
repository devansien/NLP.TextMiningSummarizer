import datetime
import file_reader as fr
import pre_processor as ps

# process starts
start_time = datetime.datetime.now()

# get text files (text level)
files = []
files = fr.get_files('data\\')
print('\n' + str(len(files)) + ' files need to be processed')

# get contents (text level)
documents = []
for f in files:
    with open(f, 'r') as file:
        documents.append(file.read())

# pre-process step 01: fix contradictions (text level)
for idx, d in enumerate(documents):
    documents[idx] = ps.fix_contractions(d)

# pre-process step 02: tokenize documents (word level)
tok_documents = []
for idx, d in enumerate(documents):
    tok_documents.append(ps.tokenize(d))

# pre-process step 03: remove non ascii characters (word level)
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

print(documents[0])
print(tok_documents)

# process ends
end_time = datetime.datetime.now()
print('\nstart  time: ' + str(start_time))
print('finish time: ' + str(end_time))
