import nltk
import os
import re
import numpy.random

GREETING_KEYWORDS = ("hello", "hi", "greetings", "hey", "what's up", "sup")

FACT_KEYWORDS = ('beach boys', 'brian wilson', 'pet sounds', 'mike love', 'good vibrations', 'god only knows', 'al jardine', 'smiley smile', 'bruce johnston', 'carl wilson')

GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    for word in sentence.words:
        if word.lower() in GREETING_KEYWORDS:
            return numpy.random.choice(GREETING_RESPONSES)

def parseSentence(sentence):
    text = nltk.word_tokenize(sentence)
    print(nltk.pos_tag(text))

print(parseSentence("Hello my name is Dawood"))