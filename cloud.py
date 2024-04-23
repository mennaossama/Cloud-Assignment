import re
from collections import Counter
from nltk.corpus import stopwords

# Download NLTK stopwords if not already downloaded
import nltk
# nltk.download('stopwords')

def remove_stopwords(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove  
    text = re.sub(r'[^\w\s]', '', text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def count_word_frequency(text):
    # Split text into words
    words = text.split()
    # Count word frequency
    word_count = Counter(words)
    return word_count

def main():
    # Read contents of the text file
    with open("C:/Users/ADMIN/Desktop/random_paragraphs.txt", 'r') as file:
        text = file.read(10000)

    # Remove stopwords from the text
    processed_text = remove_stopwords(text)

    # Count word frequency in the processed text
    word_frequency = count_word_frequency(processed_text)

    # Display word frequency count
    print("Word Frequency Count:")
    for word, count in word_frequency.items():
        print(f"{word}: {count}")

main()
