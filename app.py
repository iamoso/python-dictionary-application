import json
import difflib
from difflib import get_close_matches


def translate(word, dict):
    return dict[word]

data = json.load(open('data.json'))

while True:
    try:
        key = input("Enter key you want to find.\n").lower()
        print(translate(key, data))
        break
    except KeyError:
        possibleKeys = get_close_matches(key, data.keys())
        if not possibleKeys:
            print("The word doesn't exist. Please try again.")
        else:
            print(f"The word doesn't exist. Did You mean {possibleKeys[0]}?")
            print(translate(possibleKeys[0], data))
            break
