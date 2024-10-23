'''
this is a text-based slot machine: 
    1. it has 3 rows and 3 columns
    2. player choose to bet on 1, 2 or 3 lines (rows) of the slot machine
    3. every running time, it will generate a 3X3 matrix includes symbols (letters in this case) and their values  
    4. if there's a match on all 3 in a line, you 
    2. collect the deposit 
    3. run the game on 1 or multiple slots 
    5. balance changes  
    6. continue or the player want to quit and cash out 
'''
from limits import rows, cols, symbol_count, symbol_value
from game_logic import get_slots, check_wins
from user_side import deposit, get_number_of_lines, get_bet
from display import print_machine 



def play():
    balance = deposit() 
    original_balance = balance 
    # lines = get_number_of_lines()

        # you have money to play 
    while balance > 0: # ensure the IDENTATION is correct 
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines 

        # check if the total bet is valid  
        if total_bet > balance:
            print (f'''You do not have enough money to bet. Your balance is ${balance}. Bet again!''')
            continue
        elif total_bet == balance: 
            ask_1 = input ('Are you sure to bet all the money you have?(y/n): ')
            if ask_1.lower() != 'y': # continue
                print(f'Please bet below ${balance}.')
                continue  
            '''In order to continue playing despiting betting all the money, REMOVE the 'ELSE' function.'''

        # else: 
        print(f'You"re betting ${bet} in {lines} lines. Your total bet is ${total_bet}.')

        run = get_slots(rows, cols, symbol_count)
        print_machine(run) 
        wins, winning_line = check_wins(run, lines, bet, symbol_value)

        if wins > 0 and winning_line:
                # to print out without the brackets 
            formatted_winning_line = ', '.join(map(str, winning_line))
            print(f'You won ${wins} from line(s):', formatted_winning_line) 
                # add the profit to the balance 
            balance += wins
            print(f'Your current balance is ${balance}')
            print()
            conti_1 = input ('Do you want to keep playing?(y/n:) ') 
            # if conti_1.lower() == 'y': continue # continue the game 
            # elif conti_1.lower() == 'n':
            if conti_1.lower() != 'y': # this way, it will run the 'continue' answer and BREAK for any other answer 
                print(f'You left with ${balance}')
                print('--------------------------')
                break
        else: 
            print('You lost!')
                # substract the money 
            balance -= total_bet
            print(f'Your current balance is ${balance}')
            print()
            conti_2 = input ('Do you want to keep playing?(y/n): ') 
            # if conti_2.lower() == 'y': continue # continue the game 
            # elif conti_2.lower() == 'n':
            if conti_2 .lower() != 'y':
                print(f'You left with ${balance}')
                print('--------------------------')
                break
        
        # run out of money 
    if balance <= 0:
        print(f'Game over! You have spent all ${original_balance}!')
        if balance < 0:
                # if original_balance > balance: 
            money_owed = abs(balance) # just take the value not also the operator, remeber the correct logic 
            print(f'You are in debt ${money_owed}')
        else:   # you made profits 
            profit = balance - original_balance 
            print(f'You made ${profit}')
    

def main():
    # balance = deposit() 
    # original_balance = balance 
    while True:
        ques = input('Welcome! Do you want to play the slot machine?(y/n): ')
        if ques.lower() == 'y':
            play()
        elif ques.lower() == 'n':
            break
        else: print('Please type a valid answer.')
    
main()