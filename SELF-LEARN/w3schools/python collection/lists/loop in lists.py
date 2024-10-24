thislist = ['apple','banana','cherry']
for x in thislist : 
	print(x) 

# Specific index 
for i in range(len(thislist)):
		print(thislist [i])
		
		# use While 
while i < len(thislist):
	print(thislist [i])
	i += 1 
	
# Use COMPREHENSION 
thislist = ['apple','banana','cherry']
[print(x) for x in list] 

fruits = ['apple','banana','cherry','kiwi','mango']

    # Without if statement
newlist = [i for i in fruits]
print(newlist)

    # With if statement 
newlist = [i for i in fruits if 'a' in i]
print(newlist) 

    # Use range() and a condition 
newlist = [x for x in range(10) if x<5]

    # Can CUSTOMIZE THE OUTCOME 
newlist = [x.upper() for x in fruits]
newlist = ['hello' for x in fruits]
newlist = [x if x != 'banana' else 'orange' for x in fruits]
	# if it's banana, return orange; if not, return it 