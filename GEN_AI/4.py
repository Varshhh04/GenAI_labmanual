pip install gensim
import gensim.downloader as api
model = api.load("glove-wiki-gigaword-50")
def enrich_prompt(prompt, num_similar=3):
 words = prompt.split()
 enriched_words = []
 for word in words:
 try:
 similar_words = [w for w, _ in model.most_similar(word, topn=num_similar)]
 enriched_words.append(word + " (" + ", ".join(similar_words) + ")")
 except KeyError:
 enriched_words.append(word)
 return " ".join(enriched_words)
original_prompt = "Write a story about a Dog."
enriched_prompt = enrich_prompt(original_prompt)
print("Original Prompt:", original_prompt)
print("Enriched Prompt:", enriched_prompt)



4b:
import gensim.downloader as api
import random
# Load the GloVe model (only needs to be done once)
try:
 model = api.load("glove-wiki-gigaword-50")
except ValueError:
 print("Downloading glove-wiki-gigaword-50 model...")
 model = api.load("glove-wiki-gigaword-50")
def enrich_prompt(prompt, num_similar=3):
 """
 Enriches a prompt by adding similar words to each word in the prompt.
 Args:
 prompt (str): The original prompt.
 num_similar (int): The number of similar words to add.
 Returns:
 str: The enriched prompt.
 """
 words = prompt.split()
 enriched_words = []
 for word in words:
 try:
 similar_words = [w for w, _ in model.most_similar(word, topn=num_similar)]
 enriched_words.append(word + " (" + ", ".join(similar_words) + ")")
 except KeyError:
 enriched_words.append(word)
 return " ".join(enriched_words)
def generate_story(prompt, length=100):
 """
 Generates a simple story based on a prompt. This is a VERY basic
 example and does not use any advanced language models. It's just
 to illustrate the difference in story content.
 Args:
 prompt (str): The prompt to base the story on.
 length (int): The approximate length of the story in words.
 Returns:
 str: A generated story.
 """
 story = ""
 words = prompt.split()
 possible_next_words = words[:] # start with the words from the prompt
 current_word = random.choice(words)
 story += current_word + " "
 for _ in range(length - 1):
 next_word = random.choice(possible_next_words)
 story += next_word + " "
 possible_next_words.append(next_word) #add prev word
 # Add some simple logic to make the story slightly more coherent.
 if next_word in ["a", "an", "the"]:
 possible_next_words.extend(words) # Boost words from the original prompt
 if next_word in [".", "?", "!"]:
 possible_next_words.extend(words[:]) # restart with key words from prompt
 # add random meaningful words
 meaningful_words = ["happily", "suddenly", "quietly", "jumped","ran", "slept","ate", 
"thought","dreamed"]
 possible_next_words.append(random.choice(meaningful_words))
 return story + "."
# Example Usage:
original_prompt = "Write a story about a cat."
enriched_prompt = enrich_prompt(original_prompt)
print("Original Prompt:", original_prompt)
print("Enriched Prompt:", enriched_prompt)
original_story = generate_story(original_prompt)
enriched_story = generate_story(enriched_prompt)
print("\nOriginal Story:\n", original_story)
print("\nEnriched Story:\n", enriched_story)
# Compare the results
print("\nStory Lengths:")
print("Original Story:", len(original_story.split()))
print("Enriched Story:", len(enriched_story.split()))
print("\nOriginal Prompt Response Length:", len(original_prompt))
print("Enriched Prompt Response Length:", len(enriched_prompt))