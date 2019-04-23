import pickle

f=open("view_mal_struct.txt","w")

with open('mal_struct.pickle', 'rb') as handle:
	malayalam_sentence_structure = pickle .load(handle)

for key,val in malayalam_sentence_structure.items():
	f.write("\n"+key+" ==> "+str(val)+"\n\n")
