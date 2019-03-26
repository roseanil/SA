import nltk

import string
from nltk.tokenize import sent_tokenize
f=open("output3.txt","w", encoding="utf-8")
#######################################################################################
#######################################################################################
#Malayalam
#File read

mal = open('malayalam.txt', 'r').read()
f.write("Content read from the file\n"+mal)

#Tokenize the text into sentences and store it in a list
sentence_mal = sent_tokenize(mal)
f.write('\n\nTotal number of sentences: '+str(len(sentence_mal)))
#Calculate the number of words in the text
words_mal = [word.strip(string.punctuation) for word in mal.split()]
f.write("\n\nTotal number of words: "+str(len(words_mal))+"\n")
#Number of words in a sentence stored as a list/
num_words_mal = [len(sentence.split()) for sentence in sentence_mal]
for i in range(len(sentence_mal)):
	f.write("\nNumber of word in "+str(sentence_mal[i])+": "+str(num_words_mal[i]))

#Identify the unique words in the text and print the number of unique words
unique_word_mal= set(words_mal)
count_unique_word_mal = len(set(words_mal))
f.write("\n\n\nNumber of unique words: "+str(count_unique_word_mal))
f.write("\n\n\nSet of unique words: "+str(unique_word_mal))

#English
#####################################################################################
#####################################################################################
f.write("\n\n\n\nenglish\n\n\n")
eng = open('english.txt', 'r').read()
f.write("\nContent read from the file\n"+eng)

#Tokenize the text into sentences and store it in a list
sentence_eng = sent_tokenize(eng)
f.write('\n\nTotal number of sentences: '+str(len(sentence_eng)))
#Calculate the number of words in the text
words_eng = [word.strip(string.punctuation) for word in eng.split()]
f.write("\n\nTotal number of words: "+str(len(words_eng))+"\n")
#Number of words in a sentence stored as a list/
num_words_eng = [len(sentence.split()) for sentence in sentence_eng]
for i in range(len(sentence_eng)):
	f.write("\nNumber of word in "+str(sentence_eng[i])+": "+str(num_words_eng[i]))
for i in words_eng:
	print(i)
#Identify the unique words in the text and print the number of unique words
unique_word_eng= set(words_eng)
count_unique_word_eng = len(set(words_eng))
f.write("\n\n\nNumber of unique words: "+str(count_unique_word_eng))
f.write("\n\n\nSet of unique words: "+str(unique_word_eng))