import pathlib
import sys

from string import ascii_letters

""" Reads in a text file and adds all the valid, unique words to the word list.
Verifies that words only use the English alphabet, but cannot guarantee being a real word 
"""

in_path: pathlib.Path = pathlib.Path(sys.argv[1])
out_path: pathlib.Path = pathlib.Path('wordlist.txt')

words: list = sorted(
    {
        word.lower()
        for word in in_path.read_text(encoding='utf-8').split()
        if all(letters in ascii_letters for letters in word)
    },
    key=lambda word: (len(word), word),
)

out_path.write_text('\n'.join(words))
