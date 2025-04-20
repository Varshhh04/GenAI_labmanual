from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# Download stopwords if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Define the stopwords
stop_words = set(stopwords.words('english'))

# Sample domain-specific text (medical domain)
corpus = [
    "The patient was prescribed antibiotics to treat the infection.",
    "Doctors recommend regular exercise for cardiovascular health.",
    "The surgery was successful, and the patient is recovering well.",
    "Medical research focuses on finding cures for chronic diseases."
]

# Preprocess text: Tokenize and remove stopwords
tokenized_corpus = [
    [word for word in word_tokenize(sentence.lower()) if word.isalnum() and word not in stop_words]
    for sentence in corpus
]

# Train Word2Vec model
custom_model = Word2Vec(sentences=tokenized_corpus, vector_size=100, window=5, min_count=1, workers=4)

# Analyze embeddings
# Access similar words and vectors
print("Words similar to 'patient':", custom_model.wv.most_similar('patient'))
print("Vector for 'patient':", custom_model.wv['patient'])



























from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# Download stopwords if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Define the stopwords
stop_words = set(stopwords.words('english'))

# Function to preprocess text
def preprocess_text(file_path):
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Tokenize sentences and words, remove stopwords and non-alphanumeric tokens
    tokenized_sentences = [
        [word for word in word_tokenize(sentence.lower()) if word.isalnum() and word not in stop_words]
        for sentence in text.splitlines()  # Split by lines for sentence-wise tokenization
    ]
    
    # Remove empty sentences
    tokenized_sentences = [sentence for sentence in tokenized_sentences if sentence]
    return tokenized_sentences

# Specify the path to your text file
file_path = r'C:\Users\Nishanth\Downloads\medical_corpus.txt'  # Replace with the path to your 2 MB file

# Preprocess the text file
tokenized_corpus = preprocess_text(file_path)

# Train Word2Vec model
custom_model = Word2Vec(sentences=tokenized_corpus, vector_size=100, window=5, min_count=1, workers=4)

# Analyze embeddings
# Access similar words and vectors
word_to_query = 'patient'  # Replace with a word present in your text file
if word_to_query in custom_model.wv:
    print("Words similar to '{}':".format(word_to_query), custom_model.wv.most_similar(word_to_query))
    print("Vector for '{}':".format(word_to_query), custom_model.wv[word_to_query])
else:
    print(f"'{word_to_query}' not found in the vocabulary.")
