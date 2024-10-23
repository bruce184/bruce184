import random 
import time 

# these're CONTANST variables 
operators = ['+', '-', '*']
min_operand = 3
max_operand = 12
total_problems = 10 
wrong = 0


def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    exp = str(left) + " " + str(operator) + " " + str(right) 
        # eval() function: evaluate a value code (like the expression above)
    ans = eval(exp)
        # must have print() statement
    # print(exp) 
    # print(ans) 
    return exp, ans 
        # dont matter if there's a return 
# generate_problem()


input('Press enter to start!')
print('---------------------')
start_time = time.time() # give a time stamp 

# 'Main' code 
for i in range(total_problems): # ilerate through the indexes
    exp, ans = generate_problem()
    while True: 
        guess = input(f'Problem #{str(i+1)}: ' + exp + ' = ')
        if guess == str(ans): # covert to a number 
            break 
        else: print('Wrong!. Try again')

end_time = time() 
total_time = round(end_time - start_time, 2)
        
print('---------------------')
print(f'Well done! You finished in {total_time} seconds')

