# idea: normally, the list is horizontally -> by TRANSPOSING, we flip the slots vertically 
def print_machine(columns):
    # ilerate through every row 
    for row in range(len(columns[0])): # 'column[0] to make sure we have at least 1 collumn
        # print(' | '.join(column[row] for collumn in collumns))
        for i, column in enumerate(columns): #ilterate through the collumn to get the index and the value 
            if i != len(columns) - 1: # ilterate through every first-row values of each column
                # also, to make sure the last column doesn't have the pipe operator (visual purposes)   
                print(column[row], end = '|') # to make them not to move to the next after EVERY string 
            else: print(column[row], end = '') 
        
        print() # to move to the next row 
