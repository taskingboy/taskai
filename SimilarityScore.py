import collections
import math

# Get user input
print("Enter 4 sentences (press Enter after each one):")
train = [input().strip() for _ in range(4)]

doc_words_count = collections.defaultdict(lambda: 0.0)
doc_count_containing_words = collections.defaultdict(lambda: 0.0)
total_doc = float(len(train))
tfidf = [[] for _ in range(len(train))]
words = []

# Count word frequencies per document
for i in range(len(train)):
    for word in train[i].split():
        word = word.lower().strip('.,"\'!?')
        doc_words_count[word + str(i)] += 1

# Collect unique words
for text in train:
    for word in text.split():
        word = word.lower().strip('.,"\'!?')
        if word not in words:
            words.append(word)

# Count how many documents contain each word
for word in words:
    for text in train:
        text = text.lower()
        if word in text:
            doc_count_containing_words[word] += 1

# Calculate TF-IDF for each document
for word in words:
    word = word.lower()
    for i in range(len(train)):
        tf = doc_words_count[word + str(i)]
        idf = math.log(total_doc / (doc_count_containing_words[word]))
        tfidf[i].append(tf * idf)

# Function to compute dot product of two vectors
def dotsum(a, b):
    return sum([i * j for (i, j) in zip(a, b)])

# Find the document most similar to the first one
max_similarity = 0
max_index = -1
for i in range(1, len(train)):
    similarity = dotsum(tfidf[0], tfidf[i])
    if similarity > max_similarity:
        max_similarity = similarity
        max_index = i

print(f"\nDocument most similar to the first one is: Document {max_index + 1}")
