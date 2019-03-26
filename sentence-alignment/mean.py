import nltk
import string
import csv
from nltk.tokenize import sent_tokenize
from libindic.stemmer import Stemmer
from nltk.corpus import stopwords         
from nltk.tokenize import sent_tokenize   
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet 
wordnet_lemmatizer = WordNetLemmatizer()

f=open("output.txt","w", encoding="utf-8")
f2=open("test.txt","w", encoding="utf-8")
x="\n"
#File read
mal = open('malayalam.txt', 'r').read()
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
		strings1=strings1+" "+output['stem']
	strings1=strings1+"."

#remove punctuations and stop words
strings2=""
punctuations=['?',':','!',',',';']
stopwords_mal=["ൽ","ഉം","മാ൪","ആം","കൾ"]
for i in strings1:
	if i not in punctuations and i not in stopwords_mal:
		strings2=strings2+i
print(strings2)
#tokenize into words
word_mal= strings2.split(". ")
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
eng = open('english.txt', 'r').read()
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
word_eng=temp1.split(" . ")
for i in range(len(word_eng)):
	word_eng[i]=word_eng[i].split()
word_eng.pop()
word_eng.pop()
#print(word_eng)
for i in word_eng:
	f.write(str(i))
f.write("\n")
f.write("\n")	

##############################################################
possible_translation={}

mal_list = [0] * len(word_mal)


with open('merge.csv', 'r') as csvFile:
	reader = csv.reader(csvFile)
	for i in range(len(word_eng)):
		f.write("\n")
		f.write(str(sentence_eng[i])+":")
		f.write("\n")
		mal_list = [0] * len(word_mal)
		for j in word_eng[i]:
			flag2=0
			if j.isdigit():	
				for k in range(len(word_mal)):
					for l in word_mal[k]:
						if l == j:
							mal_list[k] += 1
			else:
				flag=0
				csvFile.seek(0)
				for row in reader:
					if j.lower() == row[0].lower():	
						flag=1
						for k in range(len(word_mal)):
							for l in word_mal[k]:
								if l ==row[1]:
									flag2=1
									mal_list[k] += 1
									f.write("in "+sentence_mal[k]+":"+j+"-->"+row[1])
					elif flag2!=1:
						synonyms = []
						for syn in wordnet.synsets(j):
							for l in syn.lemmas():
								if '_' not in l.name():
									synonyms.append(l.name()) 
		f2.write(str(j)+"\t"+str(list(set(synonyms)))+"\n\n")
		m=max(mal_list)
		templist=[]
		temp=[]
		temp=[p for p,q  in enumerate(mal_list) if q == m and m >1]
		if len(temp)!=0:
			for t in temp:
				templist.append(sentence_mal[t])
		possible_translation[sentence_eng[i]]=templist

for key, value in possible_translation.items():
	f.write(str(key))
	f.write(str(value))
	f.write("\n")
	f.write("\n")
   
f.close()      
