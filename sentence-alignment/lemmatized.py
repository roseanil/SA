import nltk
import string
import csv
from nltk.tokenize import sent_tokenize
from libindic.stemmer import Stemmer
from nltk.corpus import stopwords         
from nltk.tokenize import sent_tokenize   
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from googletrans import Translator
translator = Translator()
wordnet_lemmatizer = WordNetLemmatizer()

FLAG = 0


#f is the file to write output of program
f=open("lemmatized_output.txt","w", encoding="utf-8")
#File read
mal = open('malayalam.txt', 'r').read()

stemmer = Stemmer()
sentence_mal=mal.split(".")
#lenmatize each word
strings1=""
for i in sentence_mal:
	result = stemmer.stem(language='ml_IN', text=i)
	for word, output in result.items():
		strings1=strings1+" "+output['stem']
	strings1=strings1+". "

#remove punctuations and stop words
strings2=""
punctuations=['?',':','!',',',';']
#stopwords_mal=["ൽ","ഉം","മാ൪","ആം","കൾ"]
for i in strings1:
	if i not in punctuations:
		strings2+=i
total=0
#tokenize into words
word_mal= strings2.split(".")
for i in range(len(word_mal)):
	word_mal[i]=word_mal[i].split()
	print(len(word_mal[i]))
	total+=len(word_mal[i])
print(word_mal)
word_mal.pop()
word_mal.pop()
print(total)

for i in range(len(word_mal)):
	f.write("\n"+str(sentence_mal[i])+" : "+str(word_mal[i])+"\n")
f.write("\n")





#English
#####################################################################################
#####################################################################################

#File read
eng = open('english.txt', 'r').read()

stop_words = set(stopwords.words('english'))
sentence_eng = sent_tokenize(eng) 
word_tokens = word_tokenize(eng) 
filtered_sentence = [w for w in word_tokens if not w in stop_words] 

filtered_sentence = []   
for w in word_tokens: 
	if w.lower() not in stop_words: 
		filtered_sentence.append(w) 
#print(filtered_sentence)

filtered_sentence1 = [] 
for w in filtered_sentence:
	if w not in punctuations:
		filtered_sentence1.append(w) 
#print(filtered_sentence1)
lemmatizer = WordNetLemmatizer()
for w in range(len(filtered_sentence1)):
	filtered_sentence1[w]=lemmatizer.lemmatize(filtered_sentence1[w])

temp1= " ".join(filtered_sentence1)
temp1+=" "
word_eng=temp1.split(" . ")
total=0
for i in range(len(word_eng)):
	word_eng[i]=word_eng[i].split()

word_eng.pop()
print()
for i in range(len(word_eng)):
	f.write("\n"+str(sentence_eng[i])+" : "+str(word_eng[i])+"\n")
f.write("\n")