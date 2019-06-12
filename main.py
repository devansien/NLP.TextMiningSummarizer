import nltk
import file_reader
import contractions

# get text files
files = []
files = file_reader.get_files('data\\')
print('\n' + str(len(files)) + ' files need to be processed')

# get contents into a document list
documents = []
for f in files:
    with open(f, 'r') as file:
        documents.append(file.read())

print(documents[0])
