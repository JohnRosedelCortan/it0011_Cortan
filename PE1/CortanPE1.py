import re
from collections import Counter

def filter_and_count_words(text):
    exclude_words = {"and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"}
    words = re.findall(r'\b[A-Za-z]+\b', text)
    filtered_words = [word for word in words if word.lower() not in exclude_words]
    
    word_counts = Counter(filtered_words)
    lower_case_words = sorted([word for word in word_counts if word.islower()])
    upper_case_words = sorted([word for word in word_counts if word[0].isupper()])
    
    print("\nFiltered Word Counts:")
    for word in lower_case_words + upper_case_words:
        print(f"{word:<10} - {word_counts[word]}")
    
    print("\nTotal words filtered:", sum(word_counts.values()))

text = input("Enter a string statement:\n")
filter_and_count_words(text)
