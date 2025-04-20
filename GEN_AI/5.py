import gensim.downloader as api
import random

# Load the GloVe model
model = api.load("glove-wiki-gigaword-50")

def generate_sentence(seed_word, num_words=10):
    """Generates a sentence starting with a seed word."""
    sentence = [seed_word.capitalize()]  # Capitalize the first word
    
    for _ in range(num_words - 1):
        try:
            similar_words = [w for w, _ in model.most_similar(seed_word, topn=5)]
            next_word = random.choice(similar_words)
            sentence.append(next_word)
            seed_word = next_word
        except KeyError:
            break  # Stop if a word is not found
            
    return " ".join(sentence) + "."

def generate_paragraph(seed_word, num_sentences=3):
    para = ""
    
    for _ in range(num_sentences):
        para += generate_sentence(seed_word) + " "  # Building the paragraph
        
        try:
            similar_words = [w for w, _ in model.most_similar(seed_word, topn=5)]
            seed_word = random.choice(similar_words)
        except KeyError:
            break
            
    return para.strip()  # Remove any trailing whitespace

# Example usage
seed_word = "travel"
sentence = generate_sentence(seed_word)
print("Generated Sentence:", sentence)
print("Generated Paragraph:\n", generate_paragraph(seed_word, num_sentences=3))