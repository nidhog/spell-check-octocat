# spellcheck.py
# Spell correction made easy with python

import sys
import re
import collections

theABC = 'abcdefghijklmnopqrstuvwxyz'

file_destination = raw_input('Please enter the destination of the dictionary: ')
if(not(len(file_destination)>0)):
    file_destination = 'angry_bird.txt'

def dictionary(txt):
    return re.findall('[a-z]+', txt.lower()) 

def iKnowThis(words): return set(w for w in words if w in WIERDWORD)

def learn(features):
    top_model = collections.defaultdict(lambda: 1)
    for f in features:
        top_model[f] += 1
    return top_model

WIERDWORD = learn(dictionary(file(file_destination).read()))

def changeIt(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in theABC if b]
   inserts    = [a + c + b     for a, b in splits for c in theABC]
   return set(deletes + transposes + replaces + inserts)

def changeItAgain(word):
    return set(e2 for e1 in changeIt(word) for e2 in changeIt(e1) if e2 in WIERDWORD)

def correct(word):
    candidates = iKnowThis([word]) or iKnowThis(changeIt(word)) or changeItAgain(word) or [word]
    return max(candidates, key=WIERDWORD.get)

print 'Please enter the word you want to check:'
wurd = raw_input('_ ')
print '''Correct spelling: "''', correct(wurd),'''"'''
