import pickle
import string
from libindic.stemmer import Stemmer

#--------get malayalm text---------
mal_sent=open("malayalam.txt","r").read()


#-------clean malayalam-------
#-------store cleaned malayalam sentence in clean_mal------
mal_sent=mal_sent.strip()
mal_sent+=" "
punctuations=['?',':','!',',',';']
clean_mal=mal_sent.translate({ord(x): "" for x in punctuations})


#--------split into sentenses--------
mal_sent=mal_sent.split(". ")
mal_sent.pop()
# print(len(mal_sent))
clean_mal=clean_mal.split(". ")
clean_mal.pop()


#---------------lemmatize and store in lemmatized_sent-----------
lemmatized_sent=[]
stemmer = Stemmer()
for i in clean_mal:
	x=[]
	result = stemmer.stem(language='ml_IN', text=i)
	for word,output in result.items():
		# print(word,":",output['stem'])
		x.append(output['stem'])	
	lemmatized_sent.append(x)
# lemmatized_sent.pop()

for i in range(len(lemmatized_sent)):
	while("" in lemmatized_sent[i]): 
		lemmatized_sent[i].remove("") 


#------store for pickling------
with open('malayalam_lemma.pickle', 'wb') as f:
	pickle.dump(lemmatized_sent, f)	


#-------get tagged  malayalam file---------
mal_tag = open("tagged_file.txt", "r").read()

#-----------clean and split malayalam tagged file------------- 

mal_tag= mal_tag.strip()
t=mal_tag.split("\n")
x=[]
temp=[]
for i in t:
	if "." in i:
		i=i.replace(".", "")
		s=tuple(i.split("\\"))
		temp.append(s)
		x.append(temp)
		temp=[]
	else:
		s=tuple(i.split("\\"))
		temp.append(s)


#--------dictionary 'mal_structure' to store  malayalam sentence with tag------- 
mal_structure={}
for i in range(len(x)):
	mal_structure[mal_sent[i]]=x[i]



#----------pickling the malayalam sentence structure-----
with open('mal_struct.pickle', 'wb') as handle:
    pickle.dump(mal_structure, handle, protocol=pickle.HIGHEST_PROTOCOL)
