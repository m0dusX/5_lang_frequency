import sys
import re
from difflib import get_close_matches
from operator import itemgetter
from collections import OrderedDict


def load_data(filepath):
    with open(filepath, 'r', encoding="utf-8") as text:
        return text.read().lower()


def get_most_frequent_words(text):
    """Print list of most frequent words in loaded txt file.

    Uses regex to find all words in text and writes them and their frequency 
    to dictionary. Then it uses get_close_matches function from difflib to 
    exclude words with same basis but with different endings, for e.g. 
    dictionary and dictionaries, or "текст", "текста", "тексту" in russian.
    Then it sorts dictionary and prints it to console.

    """
    frequency = {}
    match_pattern = re.findall(r'\w+', text)
    for word in match_pattern:
        counter = frequency.get(word, 0)
        frequency[word] = counter + 1
    value_list = frequency.keys()
    for word in list(value_list):
        matches = get_close_matches(word, value_list, n = 5, cutoff=0.8)
        base_word = min(matches)
        matches.remove(base_word)
        for similar_word in matches:
            frequency[base_word] += frequency.pop(similar_word)
    sorted_tuple_list = sorted(frequency.items(), key=itemgetter(1), reverse=True)
    del sorted_tuple_list[10:]
    print("Results: ")
    for idx, word_tuple in enumerate(sorted_tuple_list, 1):
        print("{}) {}: {}".format(idx, word_tuple[0], word_tuple[1]))
        


if __name__ == '__main__':
    get_most_frequent_words(load_data(sys.argv[1]))
