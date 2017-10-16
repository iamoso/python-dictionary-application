import json


def translate(word, dict):
    return dict[word]

data = json.load(open("data.json"))

while True:
    try:
        key = input("Enter key you want to find.\n").lower()
        print(translate(key, data))
        break
    except KeyError:
        print("There's no such key. Please try again.")
