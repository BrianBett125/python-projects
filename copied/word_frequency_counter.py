from collections import Counter
import re

def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            # Remove punctuation and split into words
            words = re.findall(r'\b\w+\b', text)
            word_count = Counter(words)
            return word_count
    except FileNotFoundError:
        print("File not found.")
        return {}

# Example usage
filename = "sample.txt"  # Make sure this file exists in the same directory
word_counts = count_words_in_file(filename)

# Display top 10 most common words
print("Top 10 most common words:")
for word, count in word_counts.most_common(10):
    print(f"{word}: {count}")

