'''
return True or False
Amost any values is True
empty (strings, tuple, lists,….), empty values ( 0, (), {}, [], “”, False) are False
'''

# Compare 
print(10==9)
print(10>9)
print(10<9)

# Using if statement 
a = 220
b= 33
if b>a:
	print('b is greater than a')
else: 
	print('a is greater than b')

# Evaluate 
print(bool('hi'))
print(bool(15))

# A function inside a class that defines to False -> booleans in functions
class myclass():
	def _len_(self):
		return 0
		
myobj = myclass()
print(bool(myobj()))