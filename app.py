import json
import difflib
from difflib import get_close_matches


def translate(word, dict):
    if word in dict:
        for value in dict[word]:
            print(f"- {value}")
    elif get_close_matches(key, dict.keys(), cutoff=0.75):
        possibleKeys = get_close_matches(key, data.keys(), cutoff=0.75)
        print(f"Did You mean {possibleKeys[0]}?")
        for value in dict[possibleKeys[0]]:
            print(f"- {value}")
    else:
        print("The word doesn't exist. Please try again.")


data = json.load(open('data.json'))

key = input("Enter key you want to find.\n").lower()
translate(key, data)
