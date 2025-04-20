import gensim.downloader as api
from numpy import dot
from numpy.linalg import norm

# Load the pre-trained Word2Vec model
model = api.load('word2vec-google-news-300')

# Get word vectors
king_vector = model['king']
man_vector = model['man']
woman_vector = model['woman']

# Perform vector arithmetic (king - man + woman)
result_vector = king_vector - man_vector + woman_vector

# Find the closest word to the result vector
result = model.most_similar([result_vector], topn=1)
print(f"Result of 'king - man + woman': {result[0][0]}")

# Calculate cosine similarity between 'king - man + woman' and 'queen'
queen_vector = model['queen']
cosine_sim = dot(result_vector, queen_vector) / (norm(result_vector) * norm(queen_vector))
print(f"Cosine similarity between 'king - man + woman' and 'queen': {cosine_sim:.4f}")

# Compare with other words
words_to_compare = ['queen', 'king', 'man', 'woman', 'empress']
similarities = {}

for word in words_to_compare:
    word_vector = model[word]
    cosine_sim = dot(result_vector, word_vector) / (norm(result_vector) * norm(word_vector))
    similarities[word] = cosine_sim

print("\nCosine similarities with result vector:")
for word, sim in similarities.items():
    print(f"{word}: {sim:.4f}")
