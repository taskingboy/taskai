import re
import sys
from collections import Counter

def load_corpus(filename):
    """Loads the corpus file and builds a word frequency dictionary."""
    word_freq = Counter()
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if "END-OF-CORPUS" in line:
                break
            words = re.findall(r"[a-zA-Z'-]+", line.lower())
            word_freq.update(words)
    return word_freq

def edit_distance_one(word):
    """Generates all possible words that are one edit distance away."""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    return set(deletes + replaces + inserts + transposes)

def correct_word(word, word_freq):
    """Finds the most likely correct word from the corpus."""
    if word in word_freq:
        return word  # Word is already correct
    candidates = [w for w in edit_distance_one(word) if w in word_freq]
    if candidates:
        return min(candidates, key=lambda w: (-word_freq[w], w))  # Most frequent, then lexicographically smallest
    return word  # No suggestions found, return original word

def main():
    corpus_filename = "corpus.txt"  # Ensure this file exists with valid content
    word_freq = load_corpus(corpus_filename)

    N = int(input("Enter number of words to check: "))
    for _ in range(N):
        word = input("Enter word: ").strip().lower()
        corrected = correct_word(word, word_freq)
        print(f"Suggested correction: {corrected}")

if __name__ == "__main__":
    main()
