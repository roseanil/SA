import pickle
f=open("view_lemmatized.txt","w")

with open('malayalam_lemma.pickle', 'rb') as handle:
	lemmatized = pickle .load(handle)

for i in lemmatized:
	f.write(str(i)+"\n\n")

