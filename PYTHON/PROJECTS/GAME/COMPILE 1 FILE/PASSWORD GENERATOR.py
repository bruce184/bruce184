import random 
import string # to grab the characters 


def generate(min_len, numbers = True, special_char = True):
    # all the possible characters 
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Create a string that contains all the possible selected characters 
        # because there're always letters
    characters = letters
        # Add the rest 2 to the string (Because we set it True for numbers and special_char) 
    if numbers: 
        # Add digits to the string
        characters += digits
    if special_char: 
        # Add special characters to the string 
        characters += special

    pwd = ''
    meet_criteria = False 
    has_number = False 
    has_special = False 

    while not meet_criteria or len(pwd) < min_len: 
        # Random a new letter
        new_char = random.choice(characters)
        # Add it into the password 
        pwd += new_char 

        # Now, because we have letters, numbers, and special characters in the string 
        # We go thourgh each case if that char kind is present in the password 
        if new_char in digits: 
            has_number = True
        elif new_char in special: 
            has_special = True 

        # Set this to True 
        meet_criteria = True
        # If we include numbers, it is True 
        if numbers: 
            meet_criteria = has_number 
        # If we include special char, meaning the step above is False -> doens't matter what 'has_special' is -> set it back to True 
        # If we dont include special characters, it will be False 
        if special_char:
            meet_criteria = meet_criteria and has_special 
    
    return pwd 


def main():
    # Ask the user's preference 
    min_len = int(input ('Enter the minimum length of the password: '))
    has_numbers = input('Do you want the password to have numbers?(y/n): ').lower() == 'y' # shorter syntax 
    has_special_char = input('Do you want the password to have special characters?(y/n): ').lower() == 'y'
    pwd = generate(min_len, has_numbers, has_special_char)
    print(f'The generated password is: {pwd}')

if __name__ == '__main__':
    main()
        
    
    


