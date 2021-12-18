print("\nEdula Vinay Kumar Reddy, 19BCE0202 \n")
import nltk
s=input('Enter the file name which contains a sentence: ')
file1=open(s)
sentence = file1.read()
file1.close()
p=input('Enter the file name which contains a paragraph: ')
file2 = open(p)
paragraph = file2.read()
file2.close()
import urllib.request
from bs4 import BeautifulSoup
url=input('Enter URL of Webpage: ')
print( '\n' )
url_request = urllib.request.Request(url)
url_response = urllib.request.urlopen(url)
webpage_data = url_response.read()
soup=BeautifulSoup(webpage_data, 'html.parser')
print('<------------------------------------------Initial Contents of Sentence
are-------------------------------------------> \n')
print(sentence)
print( '\n' )
print('<------------------------------------------Initial Contents of
Paragraph are-------------------------------------------> \n')
print(paragraph)
print( '\n' )
print('<------------------------------------------Initial Contents of Webpage
are---------------------------------------------> \n')
print(soup)
print( '\n' )
web_page_paragraph_contents=soup('p')
web_page_data = ''
for para in web_page_paragraph_contents:
 web_page_data = web_page_data + str(para.text)
print('<------------------------------------------Contents enclosed between
the paragraph tags in the web page are----------------------------------------
-----> \n')
print(web_page_data)
print('\n')
from nltk.tokenize import word_tokenize
import re
sentence_without_punctuations = re.sub(r'[^\w\s]', '', sentence)
paragraph_without_punctuations =re.sub(r'[^\w\s]', '', paragraph)
web_page_paragraphs_without_punctuations =re.sub(r'[^\w\s]', '',
web_page_data)
print('<------------------------------------------Contents of sentence after
removing punctuations---------------------------------------------> \n')
print(sentence_without_punctuations)
print('\n')
print('<------------------------------------------Contents of paragraph after
removing punctuations---------------------------------------------> \n')
print(paragraph_without_punctuations)
print('\n')
print('<------------------------------------------Contents of webpage after
removing punctuations-----------------------------------------------> \n')
print(web_page_paragraphs_without_punctuations)
print('\n')
sentence_after_tokenizing = word_tokenize(sentence_without_punctuations)
paragraph_after_tokenizing = word_tokenize(paragraph_without_punctuations)
webpage_after_tokenizing =
word_tokenize(web_page_paragraphs_without_punctuations)
print('<------------------------------------------Contents of sentence after
tokenizing----------------------------------------------> \n')
print(sentence_after_tokenizing)
print( '\n' )
print('<------------------------------------------Contents of paragraph after
tokenizing---------------------------------------------> \n')
print(paragraph_after_tokenizing)
print( '\n' )
print('<------------------------------------------Contents of webpage after
tokenizing-----------------------------------------------> \n')
print(webpage_after_tokenizing)
print( '\n' )
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk_stop_words = stopwords.words('english')
sentence_without_stopwords = [i for i in sentence_after_tokenizing if not
i.lower() in nltk_stop_words]
paragraph_without_stopwords = [j for j in paragraph_after_tokenizing if not
j.lower() in nltk_stop_words]
webpage_without_stopwords = [k for k in webpage_after_tokenizing if not
k.lower() in nltk_stop_words]
print('<------------------------------------------Contents of sentence after
removing stopwords---------------------------------------------> \n')
print(sentence_without_stopwords)
print( '\n' )
print('<------------------------------------------Contents of paragraph after
removing stopwords---------------------------------------------> \n')
print(paragraph_without_stopwords)
print( '\n' )
print('<------------------------------------------Contents of webpage after
removing stopwords-----------------------------------------------> \n')
print(webpage_without_stopwords)
print( '\n' )
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
sentence_after_stemming= []
paragraph_after_stemming =[]
webpage_after_stemming = [] #creating empty lists for storing stemmed words
for word in sentence_without_stopwords:
 sentence_after_stemming.append(stemmer.stem(word))
for word in paragraph_without_stopwords:
 paragraph_after_stemming.append(stemmer.stem(word))
for word in webpage_without_stopwords:
 webpage_after_stemming.append(stemmer.stem(word))
print('<------------------------------------------Contents of sentence after
doing stemming---------------------------------------------> \n')
print(sentence_after_stemming)
print( '\n' )
print('<------------------------------------------Contents of paragraph after
doing stemming---------------------------------------------> \n')
print(paragraph_after_stemming)
print( '\n' )
print('<------------------------------------------Contents of webpage after
doing stemming-----------------------------------------------> \n')
print(webpage_after_stemming)
print( '\n' )
from textblob import TextBlob
final_words_sentence=[]
final_words_paragraph=[]
final_words_webpage=[]
for i in range(len(sentence_after_stemming)):
 final_words_sentence.append(0)
 present_word=sentence_after_stemming[i]
 b=TextBlob(sentence_after_stemming[i])
 if str(b.correct()).lower() in nltk_stop_words:
 final_words_sentence[i]=present_word
 else:
 final_words_sentence[i]=str(b.correct())
print('<------------------------------------------Contents of sentence after
correcting mispelled words----------------------------------------------->
\n')
print(final_words_sentence)
print('\n')
for i in range(len(paragraph_after_stemming)):
 final_words_paragraph.append(0)
 present_word = paragraph_after_stemming[i]
 b = TextBlob(paragraph_after_stemming[i])
 if str(b.correct()).lower() in nltk_stop_words:
 final_words_paragraph[i] = present_word
 else:
 final_words_paragraph[i] = str(b.correct())
print('<------------------------------------------Contents of paragraph after
correcting mispelled words----------------------------------------------->
\n')
print(final_words_paragraph)
print('\n')
for i in range(len(webpage_after_stemming)):
 final_words_webpage.append(0)
 present_word = webpage_after_stemming[i]
 b = TextBlob(webpage_after_stemming[i])
 if str(b.correct()).lower() in nltk_stop_words:
 final_words_webpage[i] = present_word
 else:
 final_words_webpage[i] = str(b.correct())
print('<------------------------------------------Contents of webpage after
correcting mispelled words----------------------------------------------->
\n')
print(final_words_webpage)
print('\n')
from collections import Counter
sentence_count = Counter(final_words_sentence)
paragraph_count = Counter(final_words_paragraph)
webpage_count = Counter(final_words_webpage)
print('<------------------------------------------Frequency of words in
sentence ---------------------------------------------> \n')
print(sentence_count)
print( '\n' )
print('<------------------------------------------Frequency of words in
paragraph ---------------------------------------------> \n')
print(paragraph_count)
print( '\n' )
print('<------------------------------------------Frequency of words in
webpage -----------------------------------------------> \n')
print(webpage_count)
