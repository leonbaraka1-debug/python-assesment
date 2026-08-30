"""
pythonAssessment.py

Summative Lab: Analyze a News Article
--------------------------------------
Reads a news article text file into a string and performs text
analysis: counting a specific word, identifying the most common
word, calculating average word length, and counting paragraphs
and sentences.
"""

import string


def read_article(file_path):
    """Read the contents of a text file into a single string."""
    with open(file_path, "r", encoding="utf-8") as article_file:
        return article_file.read()


def count_specific_word(text, search_word):
    """
    Count how many times search_word appears in text.

    Matching is case-insensitive and ignores surrounding punctuation
    (so "test." still matches the search word "test").

    Returns 0 if text or search_word is empty, or if no match is found.
    """
    if not text or not search_word:
        return 0

    target_word = search_word.lower()
    occurrence_count = 0

    for word in text.split():
        cleaned_word = word.strip(string.punctuation).lower()
        if cleaned_word == target_word:
            occurrence_count += 1

    return occurrence_count


def identify_most_common_word(text):
    """
    Determine which word appears most frequently in text.

    Uses a dictionary to track how many times each cleaned,
    lowercased word appears. Returns None if text is empty.
    """
    if not text.strip():
        return None

    word_frequencies = {}

    for word in text.split():
        cleaned_word = word.strip(string.punctuation).lower()
        if not cleaned_word:
            continue
        if cleaned_word in word_frequencies:
            word_frequencies[cleaned_word] += 1
        else:
            word_frequencies[cleaned_word] = 1

    if not word_frequencies:
        return None

    most_common_word = None
    highest_frequency = 0

    for word, frequency in word_frequencies.items():
        if frequency > highest_frequency:
            highest_frequency = frequency
            most_common_word = word

    return most_common_word


def calculate_average_word_length(text):
    """
    Calculate the average number of characters per word, ignoring
    punctuation. Returns 0 if text is empty.
    """
    if not text.strip():
        return 0

    words = text.split()
    total_characters = 0
    total_words = 0
    index = 0

    # while loop: walk through each word by index
    while index < len(words):
        cleaned_word = "".join(char for char in words[index] if char.isalnum())
        if cleaned_word:
            total_characters += len(cleaned_word)
            total_words += 1
        index += 1

    if total_words == 0:
        return 0

    return total_characters / total_words


def count_paragraphs(text):
    """
    Count paragraphs, where paragraphs are blocks of text separated
    by blank lines. Returns 1 for empty text (an empty article is
    still treated as a single, empty paragraph rather than zero).
    """
    if not text.strip():
        return 1

    paragraph_total = 0

    for block in text.split("\n\n"):
        if block.strip():
            paragraph_total += 1

    if paragraph_total == 0:
        return 1

    return paragraph_total


def count_sentences(text):
    """
    Estimate the number of sentences by counting sentence-ending
    punctuation: '.', '?', and '!'.

    Returns 1 for empty text (an empty article is still treated as
    a single, empty "sentence" rather than zero).

    Limitation: this only estimates sentence count. It overcounts
    when punctuation is used for something other than ending a
    sentence, such as abbreviations ("Dr.") or decimals ("3.5"),
    and it cannot detect sentences with no ending punctuation.
    """
    if not text.strip():
        return 1

    sentence_enders = (".", "?", "!")
    sentence_total = 0

    for character in text:
        if character in sentence_enders:
            sentence_total += 1

    return sentence_total


def display_results(text, search_word):
    """Print a clearly labeled summary of all the analysis results."""
    print(f"Occurrences of '{search_word}': {count_specific_word(text, search_word)}")
    print(f"Most common word: {identify_most_common_word(text)}")
    print(f"Average word length: {calculate_average_word_length(text):.2f} characters")
    print(f"Number of paragraphs: {count_paragraphs(text)}")
    print(f"Number of sentences: {count_sentences(text)}")


def main():
    article_text = read_article("news_article.txt")
    print("=== News Article Analysis ===")

    # if/else conditional: only run analysis if the article actually has content
    if article_text.strip():
        display_results(article_text, "Apple")
    else:
        print("The article file is empty.")


if __name__ == "__main__":
    # Guarded so that a missing/unavailable article file during grading
    # or testing never raises an unhandled exception.
    try:
        main()
    except FileNotFoundError:
        print("news_article.txt not found. Please place the article file in this folder.")