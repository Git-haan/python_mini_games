'''
Casino Game

Author: Ishaan Reddy
'''
import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

REEL = ['@', '#','$', '%', '&', '*']

def spin():
    random_reel = []

    for i in REEL:
        random_reel = [random.choice(REEL), random.choice(REEL), random.choice(REEL)]
    return random_reel

machine = [spin(), spin(), spin()]

def print_machine(M):
    # machine = [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
    
    print()
    print('---- SLOT MACHINE ----')
    print('----------------------')

    for row in machine:
        for element in row:
            print('|', element, '|', end ='\t')
        print()
    print()


def deposit():
    while True:
        amount = input('Enter the amount to deposit: $')

        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                break
            else:
                print('-------------------------------------------------')
                print('WARNING: Amount must be greater than 0.')
                print('-------------------------------------------------')
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
                print('-------------------------------------------------')
                print('WARNING: Amount must be greater than 0!')
                print('-------------------------------------------------')
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

            if bet > MIN_BET:
                pass
            else:
                print('-------------------------------------------------')
                print(f'WARNING: The casino mandates a minumum bet of ${MIN_BET}.')
                print('-------------------------------------------------')
                print()
                continue

            if bet <= MAX_BET:
                break
            else:
                print('-------------------------------------------------')
                print(f'WARNING: The casino mandates a maximum bet of ${MAX_BET}.')
                print('-------------------------------------------------')
                print()
                continue
        else:
            print('-------------------------------------------------')
            print('WARNING: Please enter a valid number.')
            print('-------------------------------------------------')
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
