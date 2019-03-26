import nltk

import string
from nltk.tokenize import sent_tokenize

#######################################################################################
#######################################################################################
#Malayalam
######################################################################################
######################################################################################
#File read

mal = open('malayalam.txt', 'r').read()
#print("Content read from the file: ",mal)

#Tokenize the text into sentences and store it in a list
sentence_mal = sent_tokenize(mal)

#print('Number of sentences: ',len(sentence_mal))


#Calculate the number of words in the text
words_mal = [word.strip(string.punctuation) for word in mal.split()]
#print("Number of words: ",len(words_mal))

#Number of words in a sentence stored as a list/
num_words_mal = [len(sentence.split()) for sentence in sentence_mal]
#print('Number of word in each sentence: ',num_words_mal)

#Identify the unique words in the text and print the number of unique words
unique_word_mal= set(words_mal)
count_unique_word_mal = len(set(words_mal))
#print("Number of unique words: ",count_unique_word_mal)
#print("Set of unique words: ",unique_word_mal)

#####################################################################################
#####################################################################################
#English
#####################################################################################
#####################################################################################

eng = open('english.txt', 'r').read()
#print("Content read from the file: ",eng)

#Tokenize the text into sentences and store it in a list
sentence_eng = sent_tokenize(eng)
#print("List of sentences:\n\n\n")

#print('Number of sentences: ',len(sentence_eng))

#Calculate the number of words in the text
words_eng = [word.strip(string.punctuation) for word in eng.split()]
#print("Number of words: ",len(words_eng))

#Number of words in a sentence stored as a list/
num_words_eng = [len(sentence.split()) for sentence in sentence_eng]
#print('Number of word in each sentence: ',num_words_eng)

#Identify the unique words in the text and print the number of unique words
unique_word_eng= set(words_eng)
count_unique_word_eng = len(set(words_eng))
#print("Number of unique words: ",count_unique_word_eng)
#print("Set of unique words: ",unique_word_eng)

##########################################################################################################
#Length based alignment
##########################################################################################################
possible_translation={}
for i in range(len(sentence_eng)):
    templist=[]
    for j in range(len(sentence_mal)):
        if num_words_eng[i]==num_words_mal[j]:
            templist.append(sentence_mal[j])
    possible_translation[sentence_eng[i]]=templist

f=open("output.txt","a+", encoding="utf-8")

#print("Possible mappings using length baesed approach:\n")

for key, value in possible_translation.items():
    f.write(str(key))
    f.write(str(value))
    x="\n"
    f.write(x)
    f.write(x)
   
f.close()      
