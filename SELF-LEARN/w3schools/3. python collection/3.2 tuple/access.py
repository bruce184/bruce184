'''
    store **multiple items in a 1 variable** 
    tuple is **ordered (indexed), unchangeable, immutable** and **allow duplicate values** 
    use `()` 
    Basic commands are like Lists
    For those that involving ‘changing’, use workaround
'''

thistuple = ('apple','banana','cherry', 'orange','kiwi','melon','mango')
# Index 
print(thistuple[1])
print(thistuple[2:5])

# Negative index
print(thistuple[-1])
print(thistuple[-5:-1])

# Leaving out one of the ends, it will run to the end of that range 
print(thistuple[:4])
print(thistuple[2:])

# Check 
thistuple = ('apple','banana','cherry')
if 'apple' in thistuple: 
	print('Yes, "apple" is in the fruits tuple')