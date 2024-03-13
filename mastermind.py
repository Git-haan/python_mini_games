'''
Mastermind Game

Author: Ishaan Reddy
'''
import random

alphabet = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
tries = 10
code_length = 3

def generate_code():
    code = []

    for i in range(code_length):
        letter = random.choice(alphabet)
        code.append(letter)
    
    return code

def guess_code():
    while True:
        guess = input('Guess: ').upper().split(' ')

        if len(guess) != 3:
            print('You must guess 3 letters!')
            continue

        for i in guess:
            if i not in alphabet:
                print(f'Invalid letter {i}!')
                break

        else:
            break

    return guess

def check_code(guess, real_code):
    letter_count = {}
    correct_pos = 0
    incorrect_pos = 0

    for letter in real_code:
        if letter not in letter_count:
            letter_count[letter] = 0
        letter_count[letter] += 1

    # zip decomposes guess and real into comparable tuples
    for guess_letter, real_letter in zip(guess, real_code): 
        if guess_letter == real_letter:
            correct_pos += 1
            letter_count[guess_letter] -= 1

    for guess_letter, real_letter in zip(guess, real_code): 
        if guess_letter in letter_count and letter_count[guess_letter] > 0:
            incorrect_pos += 1
            letter_count[guess_letter] -= 1

    return correct_pos, incorrect_pos


def game():

    code = generate_code()

    for attempts in range(1, tries + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == code_length:
            print(f'You guessed the code in {attempts} tries!')
            break

        print(f'Correct Positions: {correct_pos} ')
        print(f'Incorrect Positions: {incorrect_pos} ')

    else:
        print(f'You ran out of tries, the code was: {code}')

# Introduction

print('Welcome to a game called Mastermind.')
print('Your goal is to guess the correct code to unlock the vault full of gold!')

example = input('Do you want to see an example [yes/no]: ')
if example == 'yes' or example == 'y':
    print('The sequence should be 3 letters with a space inbetween')
    print('For example, your input could be: A A A')
else:
    pass

if __name__ == '__main__':
    game()