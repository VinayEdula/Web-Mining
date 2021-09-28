print("\nEdula Vinay Kumar Reddy, 19BCE0202 \n")
import math
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


No_Of_Documents=3
No_of_Unique_Words=len(unqwords)
documents=[]
total_terms_doc_i=[]
documents.append(freqCountA)
documents.append(freqCountB)
documents.append(freqCountC)
total_terms_doc_i.append(len(bagOfWordsA))
total_terms_doc_i.append(len(bagOfWordsB))
total_terms_doc_i.append(len(bagOfWordsC))
tf=[]

for i in range(0, No_Of_Documents):
    tf_i=[]
    for j in range(0, No_of_Unique_Words):
        x=(documents[i][j]/total_terms_doc_i[i])
        tf_i.append(format(x,".3f"))
    tf.append(tf_i)
print('\n')



TF_Table = prettytable.PrettyTable()
unqwords.insert(0,'Document ID')
TF_Table.field_names=unqwords
TF_Table.title='TF Table'

for i in range(0, No_Of_Documents):
    tf[i].insert(0,'File '+str((i+1)))
    TF_Table.add_row(tf[i])

print(TF_Table)
for i in range(0, No_Of_Documents):
    tf[i].pop(0)
unqwords.pop(0)
print('\n')



idf=[]
for i in range(0, No_of_Unique_Words):
    count=0
    for j in range(0, No_Of_Documents):
        if(documents[j][i]>=1):
            count=count+1
    x=math.log((1 + No_Of_Documents) / count)
    idf.append(format(x,".3f"))

IDF_Table = prettytable.PrettyTable()
IDF_Table.field_names=unqwords
IDF_Table.title='IDF Table'
IDF_Table.add_row(idf)
print(IDF_Table)
print('\n')

tfidf=[]
for i in range(0, No_Of_Documents):
    tfidf_i=[]
    for j in range(0, No_of_Unique_Words):
        y=float((tf[i][j]))*float((idf[j]))
        tfidf_i.append(format(y,".3f"))
    tfidf.append(tfidf_i)


TFIDF_Table = prettytable.PrettyTable()
unqwords.insert(0,'Document ID')
TFIDF_Table.field_names=unqwords
TFIDF_Table.title='TF-IDF Table'

for i in range(0, No_Of_Documents):
    tfidf[i].insert(0, 'File ' + str((i + 1)))
    TFIDF_Table.add_row(tfidf[i])
print(TFIDF_Table)