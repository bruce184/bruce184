import random 
from limits import rows, cols, symbol_count, symbol_value


# CHECK IF THEY GET ALL 3 IN A ROW 
def check_wins(columns, lines, bet, values):
    # initialize 
    wins = 0 
    winning_line = []
    for line in range(lines): # ilterate through every line(row): line 1, line 2, line 3
        symbol = columns[0][line] # get the symbol of the FIRST column in that line 
        for column in columns:  # ilterate through every column (chạy hàng ngang)
            symbol_to_check = column[line] # get the symbol in the column of that line 
            if symbol_to_check != symbol: break # if not the same, break
        else: 
            wins += values[symbol] * bet # if same, they win 
            winning_line.append(line + 1)
    return wins, winning_line


# GENERATE THE LOOK OF THE MACHINE  
def get_slots(row, col, symbol):
    # compile all the symbols into 1 list, then to take from this list 
    all_symbols = [symbol for symbol, symbol_count in symbol.items() for _ in range(symbol_count)]
    #     # remember: each variable is signed accordinglly as the variables in the source 
    # for symbol, symbol_count in symbol.items():
    #     for _ in range(symbol_count):
    #         all_symbols.append(symbol) # ex: symbol: A, symbol_count: 2

    # add value to the collumns
    columns = [] # empty 'OVERALL' list, consists of 3 collumns 
    for _ in range(col): # ilterate through each collumn 
        column = [] # initialize an empty list 
        current_symbols = all_symbols[:] # ":" - slice operator to copy the orginal -> changes ONLY affect this list no the orginal 
        for _ in range(row): # ilterate each row
            val = random.choice(current_symbols) # get the value for a row 
            current_symbols.remove(val) # remove the first instances of that value
            column.append(val) # insert into the collumn 
        
        columns.append(column) # insert the collumn list into the OVERALL collumns list 
    
    return columns # return the OVERALL collumns list 
