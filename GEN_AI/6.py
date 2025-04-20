!pip install transformers

from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

sentences = [
    "This is a great product! I love it.",
    "I am very disappointed with this service.",
    "The weather is not okay today.but still gotta adjust the place"
]

results = classifier(sentences)
for sentence, result in zip(sentences, results):
    print(f"'{sentence}' -> Label: {result['label']}, Score: {result['score']:.3f}")