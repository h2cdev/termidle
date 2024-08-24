from termcolor import colored
import random
import mmap
from words import DICTIONARY

MAX_GUESS_ALLOWED = 6
WRONG_POSITION = 'on_yellow'
CORRECT = 'on_green'
WRONG = 'on_black'

# These 2 methods are used if words are from words.txt as one/row
#
# Load dictionary and randomly pick a word for player to guess
# def get_word_to_guess() -> str:
#     with open('./words.txt', 'r', encoding='utf-8') as f:
#         num_lines = sum(1 for _ in f)
#         line_to_use = random.randint(0, num_lines-1)
#         f.seek(line_to_use * 6)     # 5-letter word + newline = 6 bytes
#         return f.read(5)

# def validate_word(word):
#     if len(word) != 5:
#         return False    
#     with open(r'./words.txt', 'rb', 0) as f:
#         s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
#         if s.find(bytes(word, 'utf-8')) != -1:
#             return True
#         else:
#             return False
    
def get_word_to_guess() -> str:
    return DICTIONARY[random.randint(0, len(DICTIONARY))]

def validate_word(word):
    if len(word) != 5:
        return False    
    try:
        if DICTIONARY.index(word) > -1:
            return True
        else:
            return False
    except ValueError:
        return False

def prompt_for_guess(guesses) -> str:
    guess = ''
    while validate_word(guess) is not True:
        guess = input('Enter a valid 5-letter word as your guess: ')
    guesses.append(guess)
    if guess == word_to_guess:
        print_guesses(guesses)
        print(f'You won!')
        exit()
    else:
        print(f'Your guess is incorrect!')
    return guess


# Format the guess output to indicate whether the 
# letters are correct and in the right position
def format_guess(word) -> str:
    if word is None:
        return
    result = ''
    for i in range(0, 5):
        c = word[i]
        cw = word_to_guess[i]
        if c == cw:
            result += colored(c.upper(), 'white', CORRECT)
        elif c in word_to_guess:
            if word.count(c) > word_to_guess.count(c):
                result += colored(c.upper(), 'white', WRONG)
            else:
                result += colored(c.upper(), 'white', WRONG_POSITION)
        else:
            result += colored(c.upper(), 'white', WRONG)
    return result

def print_guesses(guesses):
    for word in guesses:
        print(format_guess(word))

def update_letters_status(guess):
    pass

current_guess = 0
word_to_guess = ''
all_guesses = []

word_to_guess = get_word_to_guess()

# double-letter words to test
# word_to_guess = 'teeth'
# word_to_guess = 'eases'
# word_to_guess = 'teach' #-> audio, brave, teats
for i in range(0, MAX_GUESS_ALLOWED):
    guess = prompt_for_guess(all_guesses)
    print_guesses(all_guesses)    
    update_letters_status(guess)

print(f'You have lost! The word is {word_to_guess.upper()}')
