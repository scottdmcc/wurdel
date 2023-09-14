# WURDEL

A mini "Wordle" clone that runs in the shell.

## Installation

There is only one package to install, listed in the `requirements.txt` file.

```shell
pip install -r requirements.txt
```

## Setup

There is a very basic word list supplied with the repo, `wordlist.txt`, to get you started. Once you get tired of the
same words over and over, you can use the `create_wordlist.py` app to automatically create new wordlists.

It takes a text file as input, and filters and sorts each valid, unique word and overwrites the existing word list.

In this case, "valid" just means that it's a word that only contains the 26 letters of the English alphabet. All bets
are off on whether or not the word is an actual word found in the dictionary.

There are two sample files to experiment with; the works of Sherlock Holmes and the works of Winnie the Pooh.

### Usage

```shell
python create_wordlist.py <name-of-file>
```

## Playing the game

To start the game, just run the main file:

```shell
python wurdel.py
```

The game creates a simple UI showing user guesses, and the letters tried. You have 6 attempts to guess a 5-letter word.

```text
───────────  🔠 Guess 1 🔠  ────────────
                 _____
                 _____
                 _____
                 _____
                 _____
                 _____

       ABCDEFGHIJKLMNOPQRSTUVWXYZ

Guess word:
```

Type in a 5-letter word (or just 5 letters as there is no dictionary to judge you) and hit enter. The display will
refresh showing your word, which letters are in the correct place (in green), which letters are in the word but not in
the correct spot (in yellow), and which letters are not in the word at all (in gray).

At the bottom, the alphabet will also show the color-coded values so you can see what you haven't tried yet.

If you figure out the word before all 6 attempts are made, you will get a congratulations. Otherwise, the game will
show you the correct word.

Every time you play it choses a random word (including possibly the same as your previous game) so you can play as much
as you wish.

## Customization

When a word list is generated, it includes words of all lengths, so there exists the ability to change the letter count
for the game.

At the top of the file are a few constants that can easily be changed to modify the game:

- `WORD_LENGTH` is how many letters the word should have. Too many letters will mean a shorter list of possibilities.
- `TOTAL_GUESSES` is how many guesses the user gets to guess the mystery word.

There is also `STYLE_GUIDE` that has the colors used throughout the game. Check out 
[the documentation](https://rich.readthedocs.io/en/stable/markup.html) for `rich` if you'd like to learn how to change
the colors.
