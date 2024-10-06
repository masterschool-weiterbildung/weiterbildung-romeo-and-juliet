from romeo_and_juliet import PLAY
from collections import Counter

TOP_FREQUENT_WORDS = 200

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
    Processes the input text and returns a list of sanitized words.

    This function do the following:
        1. Splits the input text by lines, then by spaces to extract words.
        2. Splits each word by periods (".") to handle any trailing
           punctuation.
        e. Excludes empty strings, lines with only whitespace,
           and period characters.

    Parameter:
        text (str): The input text to be processed.

    Returns:
        list[str]: A list of sanitized words with punctuation
        and empty entries removed.
    """
    return [sanitize_word
            for line in text.split('\n')
            for word in line.split(" ")
            for sanitize_word in word.split(".")
            if line.strip()
            and word != ''
            and sanitize_word != '.'
            and sanitize_word != ''
            and sanitize_word != '[_Exeunt'
            and sanitize_word != '[_Exit'
            and sanitize_word != '_]'
            ]

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