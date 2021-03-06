import sys
import re
from collections import Counter


def load_text_lowercase(filepath):
    with open(filepath, 'r', encoding="utf-8") as text:
        return text.read().lower()


def get_most_frequent_words(text):
    word_rank = 10
    words = re.findall(r'\w+', text)
    frequency_tuplelist = Counter(words).most_common(word_rank)
    return frequency_tuplelist


if __name__ == '__main__':
    results = get_most_frequent_words(load_text_lowercase(sys.argv[1]))
    print("Results: ")
    for word in results:
        print("{} : {}".format(word[0], word[1]))
    sys.exit()
