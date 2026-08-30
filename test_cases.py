"""
test_cases.py

Manual test cases for text_analysis.py, as required by the
assessment ("create at least three small test examples where you
already know the expected result"). Run this file directly to see
each test's actual result printed next to its expected result.
"""

from text_analysis import (
    count_specific_word,
    identify_most_common_word,
    calculate_average_word_length,
    count_paragraphs,
    count_sentences,
)


def run_test(description, actual, expected):
    status = "PASS" if actual == expected else "FAIL"
    print(f"[{status}] {description}")
    print(f"        expected: {expected!r}, got: {actual!r}")


def main():
    # 1. Search word that is present
    sample_text = "The apple pie was the best pie I have ever eaten."
    run_test(
        "Search word 'pie' is present (2 occurrences)",
        count_specific_word(sample_text, "pie"),
        2,
    )

    # 2. Search word that is absent
    run_test(
        "Search word 'banana' is absent",
        count_specific_word(sample_text, "banana"),
        0,
    )

    # 3. Different capitalization and punctuation
    punctuation_text = "Apple, apple! APPLE? apple."
    run_test(
        "Search is case-insensitive and ignores punctuation",
        count_specific_word(punctuation_text, "apple"),
        4,
    )

    # 4. Empty text
    run_test(
        "Empty text returns None for most common word",
        identify_most_common_word(""),
        None,
    )
    run_test(
        "Empty text returns 0 for average word length",
        calculate_average_word_length(""),
        0,
    )
    run_test(
        "Empty text returns 0 for paragraph count",
        count_paragraphs(""),
        0,
    )

    # 5. Multiple paragraphs
    multi_paragraph_text = "First paragraph here.\n\nSecond paragraph here.\n\nThird one."
    run_test(
        "Multiple paragraphs separated by blank lines",
        count_paragraphs(multi_paragraph_text),
        3,
    )

    # 6. Different sentence endings
    mixed_sentences_text = "Is this working? Yes it is! Great."
    run_test(
        "Sentences ending in '?', '!', and '.'",
        count_sentences(mixed_sentences_text),
        3,
    )


if __name__ == "__main__":
    main()