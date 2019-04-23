import pickle
f=open("view_lemmatized_eng.txt","w")

with open('english_lemma.pickle', 'rb') as handle:
	lemmatized = pickle .load(handle)

for i in lemmatized:
	f.write(str(i)+"\n\n")