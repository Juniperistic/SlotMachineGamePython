#made using this tutorial: https://youtu.be/th4OBktqK1I?si=eTdjX6h1Y26LOidK
#creating a text based slot machine
#the user deposits a certain amount of money
#allow the user to bet on either the 1st, 2nd, or 3rd lines of the slot machine
#determine if they won 

#collect user's deposit, add to balance, 
#allow to bet on line or muiltiple line, 
#determine if they won, 
#generate different items on slot machine, 
#add what they won to their balance

import random

#constants must be uppercase since they never change
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#slot machine 
ROWS = 3
COLS = 3

#symbols in a dictionary
symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else: 
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

#determine the rows, cols, and symbols in the spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        #copying a list so that when you select one of the symbols, 
        #it removes from the list so only the max number of each symbol 
        #can be selected
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    #need to change from this:
    # [A, B, C]
    # [A, A, A]
    # to this:
    # [A, A] 
    # [B, A]
    # [C, A]
    #this is known as transposing
    #range is equal to the length of columns
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            #if i is not equal to max index then print the pipe
            if i != len(columns) - 1:
                #adds a pipe to the end of the row
                print(column[row], end=" | ")
            #if i is equal to max index then don't print the pipe
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        #tells us if input is a valid whole number
        if amount.isdigit():
            #converting from string to int
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else: 
            print("Please enter a number.")

    return amount

def get_number_of_lines():
        while True:
            lines = input("Enter the number of lines to bet on (1 -" + str(MAX_LINES) + ")? ")
            #tells us if input is a valid whole number
            if lines.isdigit():
                #converting from string to int
                lines = int(lines)
                if 1 <= lines <= MAX_LINES:
                    break
                else:
                    print("Enter a valid number of lines.")
            else: 
                print("Please enter a number.")
        
        return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        #tells us if input is a valid whole number
        if amount.isdigit():
            #converting from string to int
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                #f string allows you to add constants into your string
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else: 
            print("Please enter a number.")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True: 
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    # * is the splat operator or unpack operator, it passes every single line from winning_lines list to print function
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True: 
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")
    
main()