from app.word_gen import WordGen
from art import *


def main():    
    # Print ASCII art in red
    tprint("WGPY")

    # Request URL input from the user
    url = input("Enter the URL of the website: ").strip()

    # Request word limit input (optional)
    word_limit = input("Enter the word limit (default 1000): ").strip()
    Url_limit = input("Enter the url_limit (default 20): ").strip()
    
    # Convert word limit to an integer or set to default
    if word_limit.isdigit():
        word_limit = int(word_limit)
    else:
        word_limit = 1000

    if Url_limit.isdigit():
        word_limit = int(word_limit)
    else:
        Url_limit = 20

    # Create WordGen object and fetch words
    word_gen = WordGen(url, max_words=word_limit)
    word_gen.fetch_words()

if __name__ == '__main__':
    main()

