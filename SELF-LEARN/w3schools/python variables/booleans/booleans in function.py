def myfunction1():
	return True 
print(myfunction1()) # output: True 

def myfunction2():
	return True
	
if myfunction2(): # if myfunction is true
	print('Yes')
else: 
	print('No')
	
# Python also has many build-in functions that return a boolean value, 
# like 'isinstance()'
x = 200
print(isinstance(x, int))