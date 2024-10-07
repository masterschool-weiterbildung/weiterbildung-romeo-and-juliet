from romeo_and_juliet import PLAY
from collections import Counter
import re

TOP_FREQUENT_WORDS = 50

"""
Constants:
    TOP_FREQUENT_WORDS (int): The number of top frequent words to display.

Functions:
    get_words(text: str) -> list[str]:

    words_frequency(words: list[str]) -> dict:

    top_n_words(freq: dict, n: int) -> dict:

    main()
"""

def get_words(text: str) -> list[str]:
    """
    Extracts and returns a list of words from the given text after cleaning it.

    Parameter:
        text (str): The input string from which to extract words.

    Returns:
        list[str]: A list of words extracted from the input string.
                    Each word is represented as a lowercase string.
    Explanation:
        - Converts the input string to lowercase and removes all
        characters that are not letters, digits, or spaces

        - Extracts and returns a list of words from the cleaned text,
        where a word is defined as a sequence of alphanumeric characters
        separated by word boundaries.
    """
    return re.findall(r'\b\w+\b', re.sub(r'[^A-Za-z0-9 ]+', '', text.lower().strip()))


def words_frequency(words) -> dict:
    """
    Calculates the frequency of each unique word in the input list.

    This function takes a list of words and returns a dictionary
    where the keys are the unique(using set) words and the values
    are the number of times each word appears in the list.

    Parameter:
        words (list[str]): A list of words for which to calculate frequencies.

    Returns:
        dict: A dictionary where keys are unique words and values.
    """
    return {word: words.count(word) for word in set(words)}

def top_n_words(freq, n) -> dict:
    """
    Returns the top N most frequent words from a frequency dictionary.

    This function takes a dictionary of word frequencies
    and returns the top `n` words with the highest frequency,
    using Python's `collections.Counter` to sort the words by frequency.

    Parameters:
        freq (dict): A dictionary where keys are words and values
        are their frequencies.
        n (int): The number of top frequent words to return.

    Returns:
        dict: A dictionary of the top `n` most frequent words
        and their frequencies.
    """
    counter = Counter(freq)
    return dict(counter.most_common(n))

def main() -> None:
    """
    The function processes the text of Shakespeare's *Romeo and Juliet*,
    calculates word frequencies, and prints the top 50 most frequent
    words along with their frequencies.

    Steps:
        1. Retrieves and sanitizes the words from the play.
        2. Computes the frequency of each word.
        3. Determines the top N most frequent words (N = 50).
        4. Prints the top 50 words and their respective counts.

    Returns:
        None

    """

    print(f"Top 50 most frequent words:")

    frequent_words = top_n_words(words_frequency(get_words(PLAY[:])),
                                 TOP_FREQUENT_WORDS)

    for key,val in frequent_words.items():
        print(f"{key} : {val}")

if __name__ == "__main__":

    main()