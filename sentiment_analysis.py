from transformers import pipeline

# Load sentiment analysis pipeline from Hugging Face
analyzer = pipeline("sentiment-analysis")

# Example text data
texts = [
    "I love the new design of your website!",
    "The service was terrible and the food was worse.",
    "It was okay, not great but not terrible either."
]

# Analyze each text
for text in texts:
    result = analyzer(text)[0]
    print(f"Text: {text}")
    print(f"Sentiment: {result['label']} | Confidence: {result['score']:.2f}")
    print("-" * 50)

