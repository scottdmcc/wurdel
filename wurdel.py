import contextlib
import random
from pathlib import Path
from string import ascii_letters, ascii_uppercase

from rich.console import Console
from rich.theme import Theme

WORD_LENGTH: int = 5
TOTAL_GUESSES: int = 6
WORD_LIST: Path = Path(__file__).parent / 'wordlist.txt'
STYLE_GUIDE: dict = {
    "correct": "bold white on green",
    "misplaced": "bold white on yellow",
    "wrong": "white on #666666",
    "bad": "dim",
    "lose": "bold white on red",
    "warning": "red on yellow",
    "ruler": "bold blue"
}

console = Console(width=40, theme=Theme(STYLE_GUIDE))


def main():
    word: str = get_random_word()
    guesses: list = ['_' * WORD_LENGTH] * TOTAL_GUESSES

    with contextlib.suppress(KeyboardInterrupt):
        idx: int = 0
        for idx in range(TOTAL_GUESSES):
            refresh_screen(headline=f'Guess {idx + 1}')
            show_guesses(guesses, word)

            guesses[idx]: str = guess_word(guesses[:idx])

            if guesses[idx] == word.upper():
                break

    game_over(guesses, word, idx)


def get_random_word() -> str:
    """
    Read from the generated word list file, and randomly choose a word with the correct letter count.
    If there are no valid words, show the user a warning and end the game.
    :return: string - random word of defined length
    """
    with open(WORD_LIST, 'r', encoding='utf-8') as file:
        word_list: list = [word.strip() for word in file if len(word.strip()) == WORD_LENGTH]

    try:
        return random.choice(word_list).strip().upper()
    except IndexError:
        console.print(f'There are no {WORD_LENGTH} letter words in the word list', style='warning')
        raise SystemExit


def refresh_screen(headline: str):
    """
    Clear the console and draw the header
    :param headline: string - header of display
    :return:
    """
    console.clear()
    console.rule(f'[{STYLE_GUIDE["ruler"]}] :input_latin_uppercase: {headline} :input_latin_uppercase:[/]\n')


def show_guesses(guesses: list, word: str):
    """
    Builds the display for the user.
    Includes all previous guesses and alphabet color coded for correct, misplaced, and incorrect letters
    :param guesses: list - all guesses made by the user
    :param word: str - current guess
    :return:
    """
    letter_status: dict = {letter: letter for letter in ascii_uppercase}

    guess: str
    for guess in guesses:
        styled_guess: list = []
        style: str = ""
        letter: str
        correct: str
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = STYLE_GUIDE['correct']
            elif letter in word:
                style = STYLE_GUIDE['misplaced']
            elif letter in ascii_letters:
                style = STYLE_GUIDE['wrong']
            else:
                style = STYLE_GUIDE['bad']

            styled_guess.append(f'[{style}]{letter}[/]')
            if letter != '_':
                letter_status[letter] = f'[{style}]{letter}[/]'

        console.print("".join(styled_guess), justify="center")

    console.print('\n' + ''.join(letter_status.values()), justify='center')


def guess_word(previous_guesses: list) -> str:
    """
    Takes in a users guess and performs validation before returning to game
    :param previous_guesses: list - all previous guesses
    :return: str - valid guess
    """
    guess: str = console.input('\nGuess word: ').upper()

    if guess in previous_guesses:
        console.print(f"You've already guessed {guess}.", style='warning')
        return guess_word(previous_guesses)

    if len(guess) != WORD_LENGTH:
        console.print(f'Your guess must be {WORD_LENGTH} letters.', style='warning')
        return guess_word(previous_guesses)

    invalid: str
    if any((invalid := letter) not in ascii_letters for letter in guess):
        console.print(f'Invalid letter: "{invalid}". Please stick to English letters.', style='warning')
        return guess_word(previous_guesses)

    # TODO: Import a dictionary to validate that the user's guess is a valid English word
    # This could be an issue if a word from the imported word list is not an English word

    return guess


def game_over(guesses: list, word: str, idx: int):
    """
    Screen to show when the game concludes; win or lose
    :param guesses: list - all guesses
    :param word: str - last word guessed
    :param idx: int - current guess attempt
    :return:
    """
    refresh_screen(headline='Game Over')
    show_guesses(guesses, word)

    if guesses[idx] == word:
        console.print(f'\n[{STYLE_GUIDE["correct"]}]Correct, the word is {word}[/]')
    else:
        console.print(f'\n[{STYLE_GUIDE["lose"]}]Sorry, the word was {word}[/]')


if __name__ == '__main__':
    main()
