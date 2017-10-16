import json
from difflib import get_close_matches


def translate(word, dict):
    if word in dict:
        return dict[word]
    elif word.lower() in dict:
        return dict[word.lower()]
    elif get_close_matches(key, dict.keys(), cutoff=0.75):
        possibleKeys = get_close_matches(key, data.keys(), cutoff=0.75)
        yesNo = input(f"Did You mean {possibleKeys[0]}? yes/no\n").lower()
        if yesNo == 'yes' or yesNo == 'y':
            return dict[possibleKeys[0]]
        elif yesNo == 'no' or yesNo == 'n':
            return "The word doesn't exist. Please try again."
        else:
            return "Incorrect input."
    else:
        return "The word doesn't exist. Please try again."


data = json.load(open('data.json'))

key = input("Enter key you want to find.\n")

output = translate(key, data)

if type(output) is list:
    for value in output:
        print(f"- {value}")
else:
    print(output)
