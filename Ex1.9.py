from collections import Counter
import re

def most_common_word(text):
    
    #words = re.findall(r'\b\w+\b', text.lower()) #remove non-alphabets and split text into words
    
    word_counts = Counter(words) #frequency of each word
    most_common = word_counts.most_common(1)
    
    if most_common:
        return most_common[0]
    else:
        return None
    

text = "Text is the original words and text form of a written or printed text work."
result = most_common_word(text)
print(f"The most common word is '{result[0]}' with {result[1]} occurrences.")