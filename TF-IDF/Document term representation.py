print("\nEdula Vinay Kumar Reddy, 19BCE0202 \n")
import nltk
import prettytable
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

file1=input('Enter the Name of File1 : ')
file2=input('Enter the Name of File2 : ')
file3=input('Enter the Name of File3 : ')

fhand1=open(file1)
fhand2=open(file2)
fhand3=open(file3)

documentA=fhand1.read()
documentB=fhand2.read()
documentC=fhand3.read()

documentA_without_punctuations =re.sub(r'[^\w\s]', '', documentA)
documentB_without_punctuations =re.sub(r'[^\w\s]', '', documentB)
documentC_without_punctuations =re.sub(r'[^\w\s]', '', documentC)

documentA_after_tokenizing = word_tokenize(documentA_without_punctuations)
documentB_after_tokenizing = word_tokenize(documentB_without_punctuations)
documentC_after_tokenizing = word_tokenize(documentC_without_punctuations)

nltk.download('stopwords')
nltk_stop_words = stopwords.words('english')
bagOfWordsA= [i.lower() for i in documentA_after_tokenizing if not i.lower() in nltk_stop_words]
bagOfWordsB= [i.lower() for i in documentB_after_tokenizing if not i.lower() in nltk_stop_words]
bagOfWordsC = [i.lower() for i in documentC_after_tokenizing if not i.lower() in nltk_stop_words]

uniqueWords=set(bagOfWordsA).union(set(bagOfWordsB)).union(set(bagOfWordsC))

numOfWordsA=dict.fromkeys(uniqueWords,0)
for word in bagOfWordsA:
    numOfWordsA[word]+=1

numOfWordsB=dict.fromkeys(uniqueWords,0)
for word in bagOfWordsB:
    numOfWordsB[word]+=1

numOfWordsC=dict.fromkeys(uniqueWords,0)
for word in bagOfWordsC:
    numOfWordsC[word]+=1

unqwords=[i for i in numOfWordsA.keys()]
freqCountA=[i for i in numOfWordsA.values()]
freqCountB=[i for i in numOfWordsB.values()]
freqCountC=[i for i in numOfWordsC.values()]
print('\n')

unqwords.insert(0,'Document ID')
freqCountA.insert(0,'File 1')
freqCountB.insert(0,'File 2')
freqCountC.insert(0,'File 3')
document_term_representation=prettytable.PrettyTable()
document_term_representation.title='Document Term Frequency Representation'
document_term_representation.field_names=unqwords
document_term_representation.add_row(freqCountA)
document_term_representation.add_row(freqCountB)
document_term_representation.add_row(freqCountC)
print(document_term_representation)