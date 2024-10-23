from limits import max_lines, min_bet, max_bet


# MAKE THE DEPOSIT 
def deposit():
    while True: 
        amount = input('How much would you like to deposit?: $')
        if amount.isdigit(): # check if this means a number
            amount = int(amount) # convert into a number
            if amount > 0: break
            else: print('Must be greater than 0.') 
        else: print('Please enter again!')

    return amount 
# deposit() # check if it runs 


# COLLECT THE BETTING
def get_number_of_lines():
     while True: 
        line = input(f'Enter number of lines to bet on each line (1-{max_lines})?: ')
        if line.isdigit(): # check if this means a number
            line = int(line) # convert into a number
            if 1 <= line <= max_lines: break
            else: print('Must be a valid number of lines.') 
        else: print('Please enter again!')
        
     return line


def get_bet():
    while True: 
        bet = input('What would you like to bet on each line?: $')
        if bet.isdigit(): 
            bet = int(bet)
            if min_bet <= bet <= max_bet: break 
            else: print(f'Must be between ${min_bet} and ${max_bet}.')
        else: print('Please enter a valid number.')
    
    return bet