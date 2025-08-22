# simple_wordcount_buggy.py

"""
Reads a text file and prints the top 5 most frequent words.
"""

import re
from collections import defaultdict

def read_file(path="sample.txt"):
    with open(path, "r") as f:
        return f.read()

def tokenize(text):
    return text.split()

def count_words(words):
    freq = defaultdict(int)
    for w in words:
        w = w.lower()
        freq[w] =+ 1
    return freq

def main():
    # Create a small sample file if not exists
    sample = "The quick brown fox jumps over the lazy dog. The dog sleeps."
    with open("data/sample.txt", "w") as f:
        f.write(sample)

    text = read_file("data/sample.txt")
    words = tokenize(text)
    freq = count_words(words)

    # Sort by frequency (descending)
    top = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)[:5]

    print("Top words:")
    for word, count in top:
        print(f"{word:>10} : {count}")

if __name__ == "__main__":
    main()
