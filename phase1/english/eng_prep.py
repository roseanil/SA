import nltk
import string
import pickle
from fysom import Fysom
from nltk.tag.stanford import StanfordPOSTagger
from nltk.corpus import stopwords         
from nltk.stem import WordNetLemmatizer


def SenToPhrase (tagged_sentence):
	fsm = Fysom({'initial': '0',
	                'events': [
	                {'name': 'IN', 'src': '0', 'dst': '1'},{'name': 'NN', 'src': '1', 'dst': '3'},{'name': 'NNS', 'src': '1', 'dst': '3'},
	                {'name': 'NNP', 'src': '1', 'dst': '3'},{'name': 'NNPS', 'src': '1', 'dst': '3'},{'name': 'DT', 'src': '1', 'dst': '2'},
	                {'name': 'NN', 'src': '2', 'dst': '3'},{'name': 'NNS', 'src': '2', 'dst': '3'},{'name': 'NNP', 'src': '2', 'dst': '3'},
	                {'name': 'NNPS', 'src': '2', 'dst': '3'},{'name': 'PRP$', 'src': '1', 'dst': '4'},{'name': 'PRP$', 'src': '2', 'dst': '4'},
	                {'name': 'JJ', 'src': '1', 'dst': '5'},{'name': 'JJ', 'src': '2', 'dst': '5'},{'name': 'JJR', 'src': '1', 'dst': '6'},
	                {'name': 'JJR', 'src': '2', 'dst': '6'},{'name': 'JJS', 'src': '1', 'dst': '7'},{'name': 'JJS', 'src': '2', 'dst': '7'},
	                {'name': 'NN', 'src': '5', 'dst': '3'},{'name': 'NN', 'src': '6', 'dst': '3'},{'name': 'NN', 'src': '7', 'dst': '3'},
	                {'name': 'NNS', 'src': '5', 'dst': '3'},{'name': 'NNS', 'src': '6', 'dst': '3'},{'name': 'NNS', 'src': '7', 'dst': '3'},
	                {'name': 'NNP', 'src': '5', 'dst': '3'},{'name': 'NNP', 'src': '6', 'dst': '3'},{'name': 'NNP', 'src': '7', 'dst': '3'},
	                {'name': 'NNPS', 'src': '5', 'dst': '3'},{'name': 'NNPS', 'src': '6', 'dst': '3'},{'name': 'NNPS', 'src': '7', 'dst': '3'},
	                {'name': 'PRP', 'src': '1', 'dst': '4'},{'name': 'PRP', 'src': '2', 'dst': '4'},{'name': 'NN', 'src': '4', 'dst': '3'},
	                {'name': 'NNS', 'src': '4', 'dst': '3'},{'name': 'NNP', 'src': '4', 'dst': '3'},{'name': 'NNPS', 'src': '4', 'dst': '3'},
	                {'name': 'TO', 'src': '0', 'dst': '1'},{'name': 'NN', 'src': '3', 'dst': '4'},{'name': 'NNS', 'src': '3', 'dst': '4'},
					{'name': 'NNP', 'src': '3', 'dst': '4'},{'name': 'NNPS', 'src': '3', 'dst': '4'},
	                #######VERB################
	                {'name': 'MD', 'src': '0', 'dst': '8'},{'name': 'VB', 'src': '8', 'dst': '9'},{'name': 'VBN', 'src': '9', 'dst': '21'},
					{'name': 'VBG', 'src': '9', 'dst': '10'},{'name': 'JJ', 'src': '9', 'dst': '10'},{'name': 'RB', 'src': '9', 'dst': '11'},
					{'name': 'VBD', 'src': '0', 'dst': '12'},{'name': 'VBG', 'src': '12', 'dst': '13'},{'name': 'RB', 'src': '13', 'dst': '11'},
					{'name': 'RB', 'src': '12', 'dst': '11'},{'name': 'VBN', 'src': '12', 'dst': '14'},{'name': 'VBG', 'src': '14', 'dst': '15'},
					{'name': 'JJ', 'src': '14', 'dst': '16'},{'name': 'VBZ', 'src': '0', 'dst': '17'},{'name': 'VBP', 'src': '0', 'dst': '17'},
					{'name': 'RB', 'src': '17', 'dst': '11'},{'name': 'VBG', 'src': '17', 'dst': '18'},{'name': 'VBN', 'src': '17', 'dst': '19'},
					{'name': 'RB', 'src': '18', 'dst': '11'},{'name': 'VBG', 'src': '19', 'dst': '20'},{'name': 'RB', 'src': '20', 'dst': '11'},
					{'name': 'VBG', 'src': '21', 'dst': '22'},{'name': 'RB', 'src': '14', 'dst': '11'}
	                ]})
	high_final_states = ['3','4','9','10','13','14','15','16','18','19','20','21','22']
	phras_rules={'R1':[],'R2':[],'R3':[],'R4':[],'R5':[],'R6':[],'R7':[],'R8':[],'R9':[],'R10':[],'R11':[],'R12':[]}
	to_rb = ['9','12','13','14','17','18','20']
	fsm.current = '0'
	# new_temp = ""
	t=[]
	k = 0
	phrase_count=0
	while(k<len(tagged_sentence)):
		flag = 0
		rbflag = 0
		fsm.current = '0'
		temp_current='0'
		count = 0
		# new_temp = ""
		t=[]
		j = k
		s=[]
		for j in range(k,len(tagged_sentence)):
			# print("-----For loop j----")
			# print(tagged_sentence[j])
			try:
				fsm.trigger(tagged_sentence[j][1])
				# print("\n",fsm.current)
				temp_current=fsm.current
				# new_temp += tagged_sentence[j][0] + " "
				t.append(tagged_sentence[j])
				count += 1
			except:
				break
			finally:
				if(fsm.current=='3' and j!=len(tagged_sentence)-1 and tagged_sentence[j][0][-1]!=","):
					try:
						fsm.trigger(tagged_sentence[j+1][1])
						# print(tagged_sentence[j+1])
						# print("\n",fsm.current)
						# new_temp += tagged_sentence[j+1][0] + " "
						t.append(tagged_sentence[j+1])
						count += 1
					except:
						oops = 2
				if(fsm.current=='9' and j!=len(tagged_sentence)-1):
					try:
						fsm.trigger(tagged_sentence[j+1][1])
						# print("\n",fsm.current)
						# print(tagged_sentence[j+1])
						if(fsm.current=='11'):
							fsm.current = '9'
						else:
						# new_temp += i[j+1][0] + " "
							t.append(tagged_sentence[j+1])
						count += 1
					except:
						oops = 3

				if(fsm.current=='14' and j!=len(tagged_sentence)-1):
					try:
						fsm.trigger(tagged_sentence[j+1][1])
						# print("\n",fsm.current)
						# print(tagged_sentence[j+1])
						if(fsm.current=='11'):
							fsm.current = '14'
						else:
						# new_temp += i[j+1][0] + " "
							t.append(tagged_sentence[j+1])
						count += 1
					except:
						oops = 3
				if(fsm.current=='19' and j!=len(tagged_sentence)-1):
					try:
						fsm.trigger(tagged_sentence[j+1][1])
						# print("\n",fsm.current)
						# print(tagged_sentence[j+1])
						# new_temp += i[j+1][0] + " "
						temp_current=fsm.current
						t.append(tagged_sentence[j+1])
						count += 1
					except:
						oops = 1
				if(fsm.current=='21' and j!=len(tagged_sentence)-1):
					try:
						fsm.trigger(tagged_sentence[j+1][1])
						# print("\n",fsm.current)
						# print(tagged_sentence[j+1])
						# new_temp += i[j+1][0] + " "
						t.append(tagged_sentence[j+1])
						count += 1
					except:
						oops = 1

				c=int(fsm.current)
				if(fsm.current in high_final_states):
					phrase_count+=1
					# new_temp = new_temp[:-1]
					# if(new_temp[-1]==','):
					# 	new_temp = new_temp[:-1]
					if(c==3 or c==4):
						phras_rules['R1'].append(t)
						#PREPOSITION
					elif(c==18):
						phras_rules['R2'].append(t)
						#PRESENT CONTINUOUS
					elif(c==19):
						phras_rules['R3'].append(t)
						#PRESENT PERFECT
					elif(c==20):
						phras_rules['R4'].append(t)
						#PRESENT PERFECT CONTINUOUS
					elif(c==13):
						phras_rules['R5'].append(t)
						#PAST CONTINUOUS
					elif(c==14):
						phras_rules['R6'].append(t)
						#PAST PERFECT
					elif(c==15):
						phras_rules['R7'].append(t)
						#PAST PERFECT CONTINUOUS
					elif(c==9):
						phras_rules['R8'].append(t)
						#SIMPLE FUTURE
					elif(c==10):
						phras_rules['R9'].append(t)
						#FUTURE CONTINUOUS
					elif(c==21):
						phras_rules['R10'].append(t)
						#FUTURE PERFECT
					elif(c==22):
						phras_rules['R11'].append(t)
						#FUTURE PERFECT CONTINUOUS
					t = []
					fsm.current = '0'
					# backup_k = k
					k = count + k
					flag = 1
					# break
				if(temp_current in to_rb and j!=len(tagged_sentence)-1):
					# print("----temp-----")
					# print("\n",temp_current)
					fsm.current = temp_current
					try:
						if(fsm.current=='20'):
							check = fsm.current
							s.append(tagged_sentence[j+1])
							fsm.trigger(tagged_sentence[j+2][1])
						else:
							check = fsm.current
							s.append(tagged_sentence[j])
							fsm.trigger(tagged_sentence[j+1][1])
						# print("-------ENTERED TRYYYYY-------"
						# print(tagged_sentence[j+1])
						# print("\n",fsm.current)
						if(fsm.current=='11'):
							# print("----ENTERED IF----")
							if(check=='20'):
								s.append(tagged_sentence[j+2])
							else:
								s.append(tagged_sentence[j+1])
							# count += 1
						else:
							# print("-----OOPS ELSEEE---")
							s=[]
							fsm.current =temp_current
						rbflag = 1
					except:
						# print("----Uhohhhh------")
						oops = 1
						t = []
						fsm.current = '0'
				if(fsm.current=='11'):
					phrase_count+=1
					phras_rules['R12'].append(s)
					fsm.current = '0'
					s = []
				if(flag==0):
					k += 1
				if(rbflag==1 and flag==1):
					break

	english_sentence_structure[sentence].append(phrase_count)
	english_sentence_structure[sentence].append(phras_rules)




#-------get english text------
eng_sent= open('phase1/english.txt', 'r').read()


#-------clean english-------
#-------store cleaned english sentence in clean_eng------
eng_sent=eng_sent.strip()
eng_sent+=" "
punctuations=['?',':','!',',',';']
clean_eng=eng_sent.translate({ord(x): "" for x in punctuations})


#--------split into sentenses--------
eng_sent=eng_sent.split(". ")
eng_sent.pop()
clean_eng=clean_eng.split(". ")
clean_eng.pop()


#---------remove stop words from english sentences--------
stop_words=set(['is','a','the','an','was','am','were','are','have','has','had','in','on','been','will','would','shall','should'])

#stop_words = set(stopwords.words('english'))
for j in range(len(clean_eng)):
	sentence=clean_eng[j]
	clean_eng[j]=[i for i in sentence.lower().split() if i not in stop_words]


#--------lemmatize the cleaned english sentence and store in 'lemmatized_sent'---------
lemmatized_sent=[]
lemmatizer = WordNetLemmatizer()
for i in clean_eng:
	x=[]
	for j in range(len(i)):
		x.append(lemmatizer.lemmatize(i[j]))
	lemmatized_sent.append(x)		


#------store for pickling------
with open('english_lemma.pickle', 'wb') as f:
	pickle.dump(lemmatized_sent, f)




english_sentence_structure={}
#-------------for each sentence create a sentence structure-------
for i in eng_sent:
	sentence=i
	english_sentence_structure[sentence]=[]

	#--------------add number of words to sentence structure--------
	english_sentence_structure[sentence].append(len(sentence.split()))
	
	#--------------postag each sentence---------------------
	distsim = 'english-bidirectional-distsim.tagger'
	post = 'stanford-postagger.jar'
	english_postagger = StanfordPOSTagger(distsim, post)
	postag = english_postagger.tag(sentence.split())

	#-----------add postag to sentence structure-------------
	english_sentence_structure[sentence].append(list(postag))

	#---------call fuction to get phrases---------------
	SenToPhrase(postag)

#---------store the sentence structure------------------------
with open('english_struct.pickle', 'wb') as handle:
    pickle.dump(english_sentence_structure, handle, protocol=pickle.HIGHEST_PROTOCOL)
