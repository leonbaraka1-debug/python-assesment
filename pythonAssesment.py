"""
Summative Lab: Analyze a News Article
--------------------------------------
Reads a news article text file and performs several text analysis tasks:
1. Count occurrences of a specific word
2. Identify the most common word
3. Calculate the average word length
4. Count the number of paragraphs
5. Count the number of sentences

Rubric requirements covered:
- while loop  -> used to re-prompt the user for a valid search word
- for loop    -> used inside the counting/analysis functions
- if/else     -> used throughout for conditional logic and edge cases
"""

import string


def read_article(file_path):
    """Read the contents of a text file into a string."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def count_specific_word(text, word):
    """
    Counts the number of occurrences of `word` in `text`.
    Returns 0 if no matches are found.
    """
    if not text or not word:
        return 0

    translator = str.maketrans("", "", string.punctuation)
    words = text.translate(translator).lower().split()
    search_word = word.lower()

    count = 0
    for w in words:
        if w == search_word:
            count += 1

    return count


def identify_most_common_word(text):
    """
    Identifies the most common word in `text`.
    Returns None for an empty string.
    """
    if not text:
        return None

    translator = str.maketrans("", "", string.punctuation)
    words = text.translate(translator).lower().split()

    if not words:
        return None

    word_counts = {}
    for w in words:
        if w in word_counts:
            word_counts[w] += 1
        else:
            word_counts[w] = 1

    most_common = None
    highest_count = 0
    for w, c in word_counts.items():
        if c > highest_count:
            highest_count = c
            most_common = w

    return most_common


def calculate_average_word_length(text):
    """
    Calculates the average length of words in `text`, excluding punctuation.
    Returns 0 for an empty string.
    """
    if not text:
        return 0

    translator = str.maketrans("", "", string.punctuation)
    cleaned = text.translate(translator)
    words = cleaned.split()

    if not words:
        return 0

    total_length = 0
    for w in words:
        total_length += len(w)

    return total_length / len(words)


def count_paragraphs(text):
    """
    Counts the number of paragraphs in `text`, where paragraphs are
    separated by empty lines. Returns 1 for an empty string.
    """
    if not text.strip():
        return 1

    raw_blocks = text.split("\n\n")
    paragraph_count = 0
    for block in raw_blocks:
        if block.strip():
            paragraph_count += 1

    return paragraph_count if paragraph_count > 0 else 1


def count_sentences(text):
    """
    Counts the number of sentences in `text`, based on '.', '!', '?'.
    Returns 1 for an empty string.
    """
    if not text.strip():
        return 1

    sentence_enders = ".!?"
    sentence_count = 0
    for char in text:
        if char in sentence_enders:
            sentence_count += 1

    return sentence_count if sentence_count > 0 else 1


def get_search_word():
    """
    Uses a while loop to repeatedly prompt the user until a
    non-empty search word is provided.
    """
    search_word = ""
    while search_word.strip() == "":
        search_word = input("Enter a word to search for in the article: ")
        if search_word.strip() == "":
            print("Please enter a valid, non-empty word.\n")

    return search_word.strip()


def main():
    file_path = "news_article.txt"

    try:
        article_text = read_article(file_path)
    except FileNotFoundError:
        print(f"Error: Could not find '{file_path}'. "
              f"Please make sure the file is in the same folder as this script.")
        return

    if not article_text.strip():
        print("The article file is empty. Nothing to analyze.")
        return

    print("=" * 50)
    print("       NEWS ARTICLE TEXT ANALYSIS TOOL")
    print("=" * 50)

    search_word = get_search_word()
    word_count = count_specific_word(article_text, search_word)
    print(f"\nThe word '{search_word}' appears {word_count} time(s) in the article.")

    common_word = identify_most_common_word(article_text)
    if common_word:
        print(f"The most common word in the article is: '{common_word}'")
    else:
        print("No words found to determine the most common word.")

    avg_length = calculate_average_word_length(article_text)
    print(f"The average word length is: {avg_length:.2f} characters")

    paragraph_count = count_paragraphs(article_text)
    print(f"The article contains {paragraph_count} paragraph(s).")

    sentence_count = count_sentences(article_text)
    print(f"The article contains {sentence_count} sentence(s).")

    print("=" * 50)
    print("Analysis complete.")


if __name__ == "__main__":
    main()