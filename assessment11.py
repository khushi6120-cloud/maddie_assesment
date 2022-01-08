# important imports
import numpy as np
import pandas as pd
# # import tensorflow.compat.v1 as tf
# # tf.disable_v2_behavior()
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
# Python 2.x program to transcribe an Audio file
import speech_recognition as sr

AUDIO_FILE = r"C:\Users\chris\PycharmProjects\pythonProject\imggg\voice data (3).wav"

# use the audio file as the audio source

r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    # reads the audio file. Here we use record instead of
    # listen
    audio = r.record(source)

try:
    print('The audio file contains: ' + r.recognize_google(audio))

except sr.UnknownValueError:
    print('Google Speech Recognition could not understand audio')

except sr.RequestError as e:
    print('Could not request results from Google Speech Recognition service; {0}'.format(e))
speech_test=r.recognize_google(audio)
print('speech_test')
# #  Let us assume that we got the string and that string is speech
speech_test = "then awesome ok would you be then the locking this meeting in so that we don't have more participants was once the division of team is done and structure that ok what does it is it ok if people if more people join in the game you can eat I can't we have a bird eating people why don't we start off with register rules of the game in trouble that most people would know about it should be playing codename dies it is a fun board game just enjoy yourself said they would just walk into the rules are anytime using the game for us should work just wanted longer making me want to lock the meeting that have people join in case you want to end then once you start the make a locket now will be joining as both of joining as operated but one to one among you will be joining us by Master for each of the thing that you will have read spymaster and the blue team will abuse by master and basically the aim of each team is the figure out where their agents are people in this case the blue team has 9 spy agent under 18 as 85 accident somewhere in this 25 date of birth to their location is protected by secret word and only the respective teams master no specific location for example I will I will make someone itam item Primary Ka Master"
# #
# # # print(type(speech))
# # print(type(speech_test))
# #
# # Basic preprocessing --> removal of all symbols like (),.! etc and converting all the text in lower case
corpus =[]
vacablary = []
speech = speech_test
speech = re.sub("[^a-zA-Z]", ' ', speech)
# re.sub repaces anything(string) in a string by the thing(string) mentioned by you
# re.sub(<what u want to replace>,<what u want it to be replaced by>,<source string>)
speech = speech.lower()
# converting all the character into lower case in the string
speech = speech.split()
# corpus.append(speech)
for j in range(0, len(speech)):
    vacablary.append(speech[j])

print(vacablary)

# Words per minute cal.
Time_period = 186  # sec or 3 min and 6 sec
words_per_min = (len(vacablary) * 60) / Time_period
print(words_per_min)

vacablary.sort()
#
from collections import Counter

duplicate_dict = Counter(vacablary)
print(duplicate_dict)  # to get occurence of each of the element.
print(len(speech_test))


# count the diffrent word

chars = "aaaa"
check_string = "then awesome ok would you be then the locking this meeting in so that we don't have more participants was once the division of team is done and structure that ok what does it is it ok if people if more people join in the game you can eat I can't we have a bird eating people why don't we start off with register rules of the game in trouble that most people would know about it should be playing codename dies it is a fun board game just enjoy yourself said they would just walk into the rules are anytime using the game for us should work just wanted longer making me want to lock the meeting that have people join in case you want to end then once you start the make a locket now will be joining as both of joining as operated but one to one among you will be joining us by Master for each of the thing that you will have read spymaster and the blue team will abuse by master and basically the aim of each team is the figure out where their agents are people in this case the blue team has 9 spy agent under 18 as 85 accident somewhere in this 25 date of birth to their location is protected by secret word and only the respective teams master no specific location for example I will I will make someone itam item Primary Ka Master"

for char in chars:
  count = check_string.count(char)
  if count > 1:
    print(char,count)
#
user_str=speech_test
l=user_str.split()
d={}
for i in l:
    if i not in d.keys():
        d[i] = 0
    d[i]=0
    d[i]=d[i]+1
print(d)
#
#
string=speech_test
c="aaaa"
count=0
for i in string:
    if i==c:
        count+=1
print(c,"occures",count,"times")