'''
Casino Game

Author: Ishaan Reddy
'''
import random
import time
import copy

MAX_LINES = 3
MAX_WAGER = 1000000
MIN_WAGER = 1
MIN_DEPOSIT = 10
MAX_DEPOSIT = 10000000

REEL = ['@', '#', '%']

def spin():
    random_reel = []

    for i in REEL:
        random_reel = [random.choice(REEL), random.choice(REEL), random.choice(REEL)]
    return random_reel

def print_machine(M):
    
    print()
    print('---- SLOT MACHINE ----')
    print('----------------------')
    time.sleep(2)

    for row in machine:
        for element in row:
            print('|', element, '|', end ='\t')
        print()
        time.sleep(2)
    print()
    
def check_list(M, lines):

    count = 0

    if lines == 1:
        for i in range(len(M) - 2):
            if M[i][0] == M[i][1] == M[i][2]:
                print(f'You won on line {i + 1}!')
                count += 1
            else:
                print(f'You lost on line {i + 1}!')
                count -= 1
    elif lines == 2:
        for i in range(len(M) - 1):
            if M[i][0] == M[i][1] == M[i][2]:
                print(f'You won on line {i + 1}!')
                count += 1
            else:
                print(f'You lost on line {i + 1}!')
                count -= 1
    elif lines == 3:
        for i in range(len(M)):
            if M[i][0] == M[i][1] == M[i][2]:
                print(f'You won on line {i + 1}!')
                count += 1
            else:
                print(f'You lost on line {i + 1}!')
                count -= 1

    return count

def deposit():
    while True:
        amount = input('Enter the amount to deposit: $')

        if amount.isdigit():
            amount = int(amount)

            if 10000000 > amount >= 10:
                break
            else:
                print('--------------------------------------------------------------------------------')
                print(f'WARNING: The casino mandates a deposit between ${MIN_DEPOSIT} - ${MAX_DEPOSIT}.')
                print('--------------------------------------------------------------------------------')
                print()
                continue

        else:
            print('-------------------------------------------------')
            print('WARNING: Please enter a valid number.')
            print('-------------------------------------------------')
            print()
            continue

    return amount

def get_lines():
    while True:
        lines = input(f'Enter the number of lines to bet on (1 - {MAX_LINES}): ')

        if lines.isdigit():
            lines = int(lines)

            if lines > 0:
                pass
            else:
                print('-------------------------------------------')
                print('WARNING: Amount must be greater than 0!')
                print('-------------------------------------------')
                print()
                continue

            if lines <= MAX_LINES:
                break
            else:
                print('-------------------------------------------------')
                print(f'WARNING: Maximum lines to bet on is {MAX_LINES}!')
                print('-------------------------------------------------')
                print()
                continue
        else:
            print('-------------------------------------------------')
            print('WARNING: Please enter a valid number.')
            print('-------------------------------------------------')
            print()
            continue

    return lines

def get_bet():
    while True:
        bet = input('Enter the amount to bet on each line: $')

        if bet.isdigit():
            bet = int(bet)

            if bet >= MIN_BET:
                pass
            else:
                print('----------------------------------------------------')
                print(f'WARNING: The casino mandates a minumum bet of ${MIN_BET}.')
                print('----------------------------------------------------')
                print()
                continue

            if bet <= MAX_BET:
                break
            else:
                print('--------------------------------------------------------')
                print(f'WARNING: The casino mandates a maximum bet of ${MAX_BET}.')
                print('--------------------------------------------------------')
                print()
                continue
        else:
            print('-----------------------------------------')
            print('WARNING: Please enter a valid number.')
            print('-----------------------------------------')
            print()
            continue

    return bet

def game():
    print('Welcome to CASINO ROYALE: A virtual slot machine to test your luck!')
    print()
    
    x = False
    while x == False:
    
        balance = deposit()
        lines = get_lines()
        
        while True:
            bet = get_bet()
            if (bet * lines) > balance:
                print('-------------------------------------------------')
                print(f'WARNING: You do not enough funds to bet ${bet}!')
                print('-------------------------------------------------')
                print()
            else:
                break

        print()
        print('-------------------------------------------------')
        print(f'You are betting ${bet} on {lines} lines.')
        print(f'Your total betting valuation: ${bet * lines}')
        print('-------------------------------------------------')
        confirm = input('Please confirm this valuation [YES/NO]:').lower()
        print()

        if confirm == 'yes' or confirm == 'y':
            x = True
        elif confirm == 'no' or confirm == 'n':
            print()
            continue
        else:
            print('Please type a valid input.')
            continue
    
        spin_input = input('Please type "SPIN" to activate the machine: ').lower()
        if spin_input == 'spin':
            print_machine(machine)
        else:
            print('-------------------------------------------------')
            print(f'WARNING: {spin_input} is not a valid command')
            print('-------------------------------------------------')
            print()

    print('Thank you for playing at CASINO ROYALE!')

if __name__ == '__main__':
    game()
