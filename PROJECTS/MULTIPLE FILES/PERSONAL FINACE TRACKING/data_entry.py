# Import datetime library to use datetime objects 
from datetime import datetime 

# DEFINE THE GLOBAL VARIBALES -> MORE DYNAMIC 
format = '%d-%m-%Y'
categories = {'I': 'Income', 'E': 'Expense'}


# A FUNCTION TO GET THE DATE: prompt, allow_default 
def get_date(prompt, allow_default = False):
        # 'prompt': a variable to store the user's input before give us the date 
        # 'allow_default': to return the today's date if user don't enter the date themself 
    ask = input (prompt) 
    # If they don't input the date, return today's date 
    if allow_default and not ask:  
        return datetime.today().strftime(format) # format the date
    # If they input the date 
    try: 
        valid_date = datetime.strptime(ask, format) # convert the input into a datetime object
        return valid_date.strftime(format) # convert that datetime object back into the desired-format string 
    # If they input invalidly 
    except ValueError:  
        print('Invalid date format. Please enter the data in dd-mm-yyyy format. ')
    # Recursion till the correct one 
        return get_date(prompt, allow_default) 
    

# A FUNCTION TO ASK THE BETTING AMOUNT 
def get_amount(): 
    try: 
        amount = float(input('Enter the amount: $'))
        # If they input less than 0 
        if amount <= 0: 
                # is there another way for this line???
            raise ValueError('Invalid amount. Must be greater than 0.')
        return amount
    # When they input beside numbers 
    except ValueError as e:
        print(e)
    # Recursion till the correct one 
        return get_amount()


# A FUNCTION TO CATEGORIZE THE DEPOSIT 
def get_category():
    category = input ("Enter the category ('I' for Income, 'E' for Expense): ").upper()
    # If the input is in the definition
    if category in categories:
        return categories[category]
        # else: no need for this block 
    print("Invalid option. Please enter 'I' for Income, 'E' for Expense. ")
    # Recursion till the correct one 
    return get_category()


# A FUNCTION TO ASK THE DETAILS OF THE DEPOSIT
def get_description():
    return input ('Enter the description (optional): ')
