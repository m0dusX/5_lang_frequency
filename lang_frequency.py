import sys
import re
from collections import Counter


def load_text_lowercase(filepath):
    with open(filepath, 'r', encoding="utf-8") as text:
        return text.read().lower()


def get_most_frequent_words(text):
    frequency = {}
    words= re.findall(r'\w+', text)
    print("Results: ")
    for word in Counter(words).most_common(10):
        print("{} : {}".format(word[0], word[1]))


if __name__ == '__main__':
    get_most_frequent_words(load_text_lowercase(sys.argv[1]))
