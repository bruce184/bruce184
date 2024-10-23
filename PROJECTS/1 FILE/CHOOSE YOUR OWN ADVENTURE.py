name = input ('Please type your name: ')
print(f'Welcome {name} to this adventure!')

ans = input ("You\'re\ on a dirt road, it has been come to an end and you can go left or right. Which way you like to go? ").lower()

# if choose left 
if ans == 'left':
    ans = input ('You come to a river, you can walk around or swim across. Type walk or swim: ')
    if ans == 'swim': 
        print('You swim across and were eaten by an alligator.')
    elif ans == 'walk':
        print('You walked for many miles, ran out of water and you lost the game.')
    else: 
        print('Not a valid option. You lose.')

# if choose right  
elif ans == 'right':
    ans == input ('You go back and loose.')
    if ans == 'cross': 
        ans == input ('You corss and meet a stranger. Do you want to talk to them?')
        if ans == 'yes':
            print('You talked to the stranger and they give you gold. You WIN!')
        elif ans == 'no':
            print('You ignored the stranger and they are offended. You LOSE!')
    
# if the starting ans is not left or right 
else: print('Not a valid option. You lose')



