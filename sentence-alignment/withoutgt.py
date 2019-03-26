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


#f is the file to write output of program
f=open("output3.txt","w", encoding="utf-8")
f1=open("output1.txt","w", encoding="utf-8")
#File read
mal = open('mal.txt', 'r').read()
f.write(mal)
f.write("\n")
f.write("\n")

stemmer = Stemmer()
sentence_mal=mal.split(".")
#lenmatize each word
strings1=""
for i in sentence_mal:
	result = stemmer.stem(language='ml_IN', text=i)
	for word, output in result.items():
		strings1+=" "+output['stem']
	strings1+="."

#remove punctuations and stop words
strings2=""
punctuations=['?',':','!',',',';']
stopwords_mal=["ൽ","ഉം","മാ൪","ആം","കൾ"]
for i in strings1:
	if i not in punctuations and i not in stopwords_mal:
		strings2=strings2+i

#tokenize into words
word_mal= strings2.split(".")
for i in range(len(word_mal)):
	word_mal[i]=word_mal[i].split()
word_mal.pop()
word_mal.pop()

for i in word_mal:
	f.write(str(i))
	f.write("\n")
f.write("\n")



#English
#####################################################################################
#####################################################################################

#File read
eng = open('eng.txt', 'r').read()
f.write(eng)
f.write("\n")

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
#print(filtered_sentence1)

temp1= " ".join(filtered_sentence1)
temp1+=" "
word_eng=temp1.split(" . ")
for i in range(len(word_eng)):
	word_eng[i]=word_eng[i].split()
word_eng.pop()
for i in word_eng:
	f.write(str(i))
	f.write("\n")
f.write("\n")	

########################################################
# Reading from csv file 
#word matching
no_match_eng=[]
no_match_mal=[]
possible_translation={}
numeric_match={}
dictionary_match={}
googletransmatch={}

mal_list = [0] * len(word_mal)


with open('merge.csv', 'r') as csvFile:
	reader = csv.reader(csvFile)
	for i in range(len(word_eng)):
		mal_list = [0] * len(word_mal)
		for j in word_eng[i]:
			found=0
			nosearch=0
			if j.isdigit():
				for k in range(len(word_mal)):
					for l in word_mal[k]:
						if l == j:
							found=1
							numeric_match[j]=l
							mal_list[k] += 1
			else:
				flag=0
				csvFile.seek(0)
				for row in reader:
					if j.lower() == row[0].lower():
						for k in range(len(word_mal)):
							for l in word_mal[k]:
								if l == row[1]:
									flag=1
									found=1
									dictionary_match[j]=row[1]
									mal_list[k] += 1
				'''
				if flag!=1:
					translator = Translator()
					a = translator.translate(j.lower(),dest='ml')
					for k in range(len(word_mal)):
						for l in word_mal[k]:
							if l == a.text:
								found=1
								googletransmatch[j]=a.text
								mal_list[k] += 1
		if found!=1:
			no_match_eng.append(j)
		'''
		m=max(mal_list)
		templist=[]
		temp=[]
		temp=[p for p,q  in enumerate(mal_list) if q == m and m >0]
		if len(temp)!=0:
			for t in temp:
				templist.append(sentence_mal[t])
		possible_translation[sentence_eng[i]]=templist


for key, value in possible_translation.items():
	f1.write(str(key)+str(value))
	f1.write("\n\n")
	
f.write("\n\nwords found by numeric match\n")
f.write("total:"+str(len(numeric_match))+"\n")
for key, value in numeric_match.items():
	f.write(str(key)+":"+str(value)+"\n")

f.write("\n\nwords found in dictionary\n")
f.write("total:"+str(len(dictionary_match))+"\n")
for key, value in dictionary_match.items():
	f.write(str(key)+":"+str(value)+"\n")

'''
f.write("\n\nwords found in googletransmatch\n")
f.write("total:"+str(len(googletransmatch))+"\n")
for key, value in googletransmatch.items():
	f.write(str(key)+":"+str(value)+"\n")

f.write("\n\nwords for which no match was found\n")
f.write(str(no_match_eng))
'''
f1.close()
f.close() 
