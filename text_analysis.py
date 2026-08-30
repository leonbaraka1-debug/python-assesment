"""
text_analysis.py

Python News Article Text Analysis Assessment
----------------------------------------------
Reads a news article text file into a string and performs basic
text analysis: counting a specific word, finding the most common
word, calculating average word length, and counting paragraphs
and sentences.
"""

import string


# ---------------------------------------------------------------------
# Read article
# ---------------------------------------------------------------------
def read_article(file_path):
    """Read the article file and return its full contents as a string."""
    with open(file_path, "r", encoding="utf-8") as article_file:
        return article_file.read()


# ---------------------------------------------------------------------
# 1. Count a Specific Word
# ---------------------------------------------------------------------
def count_specific_word(text, search_word):
    """
    Count how many times search_word appears in text.

    Design choice: comparison is case-insensitive (so "Apple" and
    "apple" count as the same word), and surrounding punctuation is
    stripped from each word before comparing (so "pie," still
    matches the search word "pie"). This matches how a person would
    naturally count word occurrences in an article.

    Returns 0 if the word does not appear.
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


# ---------------------------------------------------------------------
# 2. Identify the Most Common Word
# ---------------------------------------------------------------------
def identify_most_common_word(text):
    """
    Determine which word appears most frequently in text.

    Uses a dictionary to track how many times each cleaned,
    lowercased word appears, then finds the word with the highest
    count.

    Returns None if text is empty.
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


# ---------------------------------------------------------------------
# 3. Calculate Average Word Length
# ---------------------------------------------------------------------
def calculate_average_word_length(text):
    """
    Calculate total characters in the words divided by total number
    of words, ignoring punctuation.

    Returns 0 if text is empty (safe handling, avoids division by zero).
    """
    if not text.strip():
        return 0

    total_characters = 0
    total_words = 0

    for word in text.split():
        cleaned_word = "".join(char for char in word if char.isalnum())
        if cleaned_word:
            total_characters += len(cleaned_word)
            total_words += 1

    if total_words == 0:
        return 0

    return total_characters / total_words


# ---------------------------------------------------------------------
# 4. Count Paragraphs
# ---------------------------------------------------------------------
def count_paragraphs(text):
    """
    Count paragraphs, where paragraphs are blocks of text separated
    by blank lines. Empty lines themselves are not counted as
    paragraphs.
    """
    if not text.strip():
        return 0

    blocks = text.split("\n\n")
    paragraph_total = 0

    for block in blocks:
        if block.strip():
            paragraph_total += 1

    return paragraph_total


# ---------------------------------------------------------------------
# 5. Count Sentences
# ---------------------------------------------------------------------
def count_sentences(text):
    """
    Estimate the number of sentences by counting sentence-ending
    punctuation: '.', '?', and '!'.

    Limitation: this is only an estimate. It will overcount when a
    period is used for something other than ending a sentence, such
    as abbreviations ("Dr.", "U.S.") or decimal numbers (e.g. "3.5").
    It also cannot detect sentences that lack ending punctuation.
    """
    if not text.strip():
        return 0

    sentence_enders = (".", "?", "!")
    sentence_total = 0

    for character in text:
        if character in sentence_enders:
            sentence_total += 1

    return sentence_total


# ---------------------------------------------------------------------
# Display results
# ---------------------------------------------------------------------
def display_results(text, search_word):
    """Print a clearly labeled summary of all the analysis results."""
    print(f"Occurrences of '{search_word}': {count_specific_word(text, search_word)}")
    print(f"Most common word: {identify_most_common_word(text)}")
    print(f"Average word length: {calculate_average_word_length(text):.2f} characters")
    print(f"Number of paragraphs: {count_paragraphs(text)}")
    print(f"Number of sentences: {count_sentences(text)}")


# ---------------------------------------------------------------------
# Main program
# ---------------------------------------------------------------------
def main():
    article_text = read_article("news_article.txt")
    print("=== News Article Analysis ===")
    display_results(article_text, "Apple")


if __name__ == "__main__":
    main()