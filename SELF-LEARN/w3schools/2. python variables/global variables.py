# Def: variables that are created outside a function 

x = 'awesome'

# DEFINE A FUNCTION
def myfunc():
	print('Python is ' +x)
myfunc() # Call the function 

	# Declare the same one with different value 
def myfunc():
	x = 'fantastic'
	print('Python is ' +x)
myfunc()               # return with fantastic 
print('Python is ' +x) # return with awesome

	# Declare the same one with the 'global' keyword
def myfunc():
	global x 
	x = 'fantastic'
myfunc()
print('Python is' +x)