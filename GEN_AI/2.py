pip install numpy pandas matplotlib gensim scikit-learn
import numpy as np
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import gensim.downloader as api
# Load a smaller pre-trained model
model = api.load("word2vec-google-news-300") # Automatically downloads if missing
# Test similarity
print(model.most_similar("soccer", topn=5))
# Choose 10 sports-related words
words = ["soccer", "basketball", "tennis", "baseball", "football",
"hockey", "golf", "cricket", "rugby", "volleyball"]
# Extract embeddings
vectors = np.array([model[w] for w in words])
# Reduce dimensions (PCA and t-SNE)
pca_vectors = PCA(n_components=2).fit_transform(vectors)
tsne_vectors = TSNE(n_components=2, perplexity=5, 
random_state=42).fit_transform(vectors)
# Function to plot embeddings
def plot_embeddings(words, embeddings, title):
plt.figure(figsize=(6, 5))
plt.scatter(embeddings[:, 0], embeddings[:, 1], color="blue")
for word, (x, y) in zip(words, embeddings):
plt.text(x, y, word, fontsize=12)
plt.title(title)
plt.show()
# Plot PCA and t-SNE results
plot_embeddings(words, pca_vectors, "PCA - Sports Words")
plot_embeddings(words, tsne_vectors, "t-SNE - Sports Words")
# Function to find similar words
def similar_words(word, top_n=5):
return [w[0] for w in model.most_similar(word, topn=top_n)] if word in 
model else ["Word not found"]
# Example: Find words similar to "soccer"
print("Similar words to 'football':", similar_words("soccer"))
