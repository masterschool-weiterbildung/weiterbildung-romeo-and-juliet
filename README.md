# Word Frequency Analyzer for *Romeo and Juliet*

This script analyzes the word frequency in Shakespeare's *Romeo and Juliet* and identifies the top 50 most frequently occurring words.

## Features
- Cleans and extracts words from the text.
- Calculates word frequencies.
- Displays the top 50 most frequently used words.

## Requirements
- Python 3.x
- `collections.Counter`
- `re` module

## Usage
1. Ensure that `romeo_and_juliet.py` contains the variable `PLAY` with the text of the play.
2. Run the script:
   ```sh
   python script.py
   ```
3. The output will display the top 50 most frequent words and their count.

## Functions
### `get_words(text: str) -> list[str]`
Extracts and returns a list of words from the given text after cleaning it.

### `words_frequency(words: list[str]) -> dict`
Computes and returns a dictionary containing word frequencies.

### `top_n_words(freq: dict, n: int) -> dict`
Returns the top `n` most frequent words from the frequency dictionary.

### `main()`
Processes the text and displays the top 50 frequent words.

## Example Output
```
Top 50 most frequent words:
and : 345
the : 298
I : 255
...
```

