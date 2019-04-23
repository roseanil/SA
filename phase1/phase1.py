import nltk
import string
import csv
import pickle
from googletrans import Translator
from nltk.corpus import wordnet





#Output of program
f1=open("phase1.csv","w", encoding="utf-8")
f2=open("meta.txt","w", encoding="utf-8")



#-------------------------------------------------------------------
#							Malayalam
#-------------------------------------------------------------------

#---------get malayalam input and store it in sentence_mal-------------
mal_sent = open('malayalam.txt', 'r').read()
mal_sent=mal_sent.strip()
mal_sent+=" "
sentence_mal=mal_sent.split(". ")

#sentence and words without lemmatizing
intial=[]
for i in sentence_mal:
	intial.append(i.split())
intial.pop()

#sentences are striped of punctuations
#----------pickle lemmatized malayalam sentences-------------
with open('mal/malayalam_lemma.pickle', 'rb') as file:
	word_mal = pickle.load(file)


#-------------------------------------------------------------------
#							English
#-------------------------------------------------------------------


#---------get english input and store it in eng_sent-------------
eng_sent= open('english.txt', 'r').read()
eng_sent=eng_sent.strip()
eng_sent+=" "
eng_sent=eng_sent.split(". ")
eng_sent.pop()



#sentences are striped of punctuations and stopwords
#----------pickle lemmatized english sentences
with open('english/english_lemma.pickle', 'rb') as file:
	word_eng = pickle.load(file)


#store number of words in each sentence to a list
eng_count=[]
for i in word_eng:
	eng_count.append(len(i))



#-------------------------------------------------------------------
#					word mapping
#-------------------------------------------------------------------


translator = Translator(service_urls=['translate.google.co.in'])


possible_translation={}
match={}

#Reading the csv file 
with open('merge_final0.csv', 'r') as csvFile:
	reader = csv.reader(csvFile)
	for i in range(len(word_eng)):
		mal_list = [0] * len(word_mal)
		for j in word_eng[i]:
			fl=0  		#break out of dictionary
			found=0		#check if any match found
			FLAG = 0	#set if google trans doesnt work
	
			#-----------------check if numeric matching is there------------------
			if j.isdigit():
				for k in range(len(word_mal)):
					for l in range(len(word_mal[k])):
						if word_mal[k][l] == j:
							found=1
							mal_list[k] += 1
			
			else:
				#-----------------check if dictionary matching is there------------ 
				csvFile.seek(0)
				for row in reader:
					if j.lower() == row[0].lower():
						for k in range(len(word_mal)):
							for l in range(len(word_mal[k])):
								#check if word match with lemmatized word
								if word_mal[k][l] == row[1]:
									fl=1
									match[j]=word_mal[k][l]
									found=1
									mal_list[k] += 1
								#check if word match with orginal word
								elif  intial[k][l]==row[1]:
									fl=1
									match[j]=intial[k][l]
									found=1
									mal_list[k] += 1												
					if fl==1:
						break


						
				if found!=1:	
				#------------------check in google trans----------------------------			
					try:
						a = translator.translate(j,dest='ml')
						for k in range(len(word_mal)):
							for l in range(len(word_mal[k])):
								#check if word match with lemmatized word
								if word_mal[k][l] == a.text:
									match[j]=word_mal[k][l]
									found=1
									mal_list[k] += 1
								#check if word match with orginal word
								elif  intial[k][l]==a.text:
									match[j]=intial[k][l]
									found=1
									mal_list[k] += 1		
					except:
						FLAG = 1

				

				if found!=1:
				#-------------------Check the words that are not found in the synset------------------
					synonyms=[]				#list to store synonyms
					#find synonyms of words from synset
					for syn in wordnet.synsets(j):			
						for l in syn.lemmas(): 
							synonyms.append(l.name()) 
					#look for matc
					if len(synonyms)!=0:
						for z in synonyms:
							csvFile.seek(0)
							for row in reader:
								if (z.lower() == row[0].lower()):
									for k in range(len(word_mal)):
										for l in range(len(word_mal[k])):
											#check if word match with lemmatized word
											if word_mal[k][l] == row[1]:
												match[j]=word_mal[k][l]
												found=1
												mal_list[k] += 1
											#check if word match with lemmatized word
											elif intial[k][l]==row[1]:
												match[j]=intial[k][l]
												found=1
												mal_list[k] += 1	
							if found==1:
								break
		

		#----------put threshold to 60% word match--------------
		m=int(eng_count[i]*.60)
		print("Mapping sentence ",i+1)
		# print(mal_list)
		templist=[]				#to store list of sentences with score
		temp=[] 				#to store highest scores
		top_count=0
		
		#get the count of sentences that pass the score
		for d in mal_list:		
			if d>=m:			
				top_count+=1
		
		#check there are more than 3 sentence that pass the threshold 
		if top_count>3:			
			temp=[p for p,q  in enumerate(mal_list) if q>=m]
			for t in temp:
				sentence_score=sentence_mal[t]+"//"+str(mal_list[t])
				templist.append(sentence_score)
		#else take top 3 scores		
		else:					
			temp=sorted(zip(mal_list,sentence_mal), reverse=True)[:3]
			# print(temp)
			for t in temp:
				if t[0]!=0:
					sentence_score=t[1]+"//"+str(t[0])
					templist.append(sentence_score)

		#if there are matches to english sentence add to 'possible_trasnlation'
		if templist!=[]:
			possible_translation[eng_sent[i]]=templist
		
		

if(FLAG==1):
	print("Unable to access Google Translate.")


#-------------write the translations to 'phrase.csv'-----------------
print("Writing to phase1.csv")
for key, value in possible_translation.items():
	f1.write(str(key))
	for item in value:
		f1.write("\t"+str(item))
	f1.write("\n")
print("Writing to meta.txt")
for key, value in match.items():
	f2.write(str(key)+":"+str(value)+"\n")
