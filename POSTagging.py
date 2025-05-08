def pos_tag_rule_based(word):
    """Basic rule-based POS tagging."""
    word = word.lower()

    if word in ['a', 'an', 'the']:
        return 'DT'  # Determiner
    elif word.endswith('ing'):
        return 'VBG'  # Verb, gerund/present participle
    elif word.endswith('ed'):
        return 'VBD'  # Verb, past tense
    elif word.endswith('ly'):
        return 'RB'  # Adverb
    elif word.endswith(('ous', 'ful', 'ive')):
        return 'JJ'  # Adjective
    elif word in ['is', 'am', 'are', 'was', 'were']:
        return 'VB'  # Verb
    elif word in ['he', 'she', 'they', 'it', 'we', 'i']:
        return 'PRP'  # Pronoun
    elif word in ['and', 'or', 'but', 'because']:
        return 'CC'  # Conjunction
    elif word in ['on', 'in', 'at', 'with', 'from', 'to', 'of']:
        return 'IN'  # Preposition
    elif word.endswith('s') and len(word) > 1:
        return 'NNS'  # Plural noun
    else:
        return 'NN'  # Default to noun

# --------------------------
# Main Program
# --------------------------

# Get sentence input from user
sentence = input("Enter a sentence: ").strip()

# Tokenize the sentence into words
words = sentence.split()

# Tag each word and print result
print("\nTagged sentence:")
for word in words:
    tag = pos_tag_rule_based(word)
    print(f"{word}/{tag}", end=' ')
