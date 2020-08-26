import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches


opendata = open('data.json')
data = json.load(opendata)

def dictionaryMeanings(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        returnStatement =  input("Did you mean %s instead? Enter Y if yes, N if no." %get_close_matches(w, data.keys())[0])
        if returnStatement =='Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif returnStatement == 'N':
            return "The Word does not exist."
        else:
            return "Try again"
    else:
        return "This word does not exist. Please double check it."

word = input("Enter a word: ")

output = (dictionaryMeanings(word)) 

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)