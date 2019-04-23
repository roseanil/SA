import pickle

with open('english_struct.pickle', 'rb') as handle:
	english_sentence_structure = pickle .load(handle)

f=open("view_english_structure.txt","w")

for key,val in english_sentence_structure.items():
	f.write(str(key))
	for p in val:
		f.write("\n\n"+str(p))
	f.write("\n\n\n\n--------------\n")
