'''
    normally, we cannot change tuple values
    **Workaround**: covert tuple into a list, change the list, then covert back into a tuple
'''

# create tuple x 
x = ('apple','banana','cherry')
# creat a list y with list x data  
y = list(x) 
y[1] = 'kiwi' # change 
# convert back to a tuple
x = tuple(y) 
print(x)

# ADD 
thistuple1 = ('apple','banana','cherry')
y1 = list(thistuple1) # covert into a list 
y1.append('orange')  # add 
thistuple1 = tuple(y1) # convert back 

thistuple2 = ('apple','banana','cherry')
y2 = ('orange',) # MUST HAVE COMMA AFTER THE ITEM WHEN CREATE A TUPLE WITH ONE ITEM 
thistuple2 += y2
print(thistuple2) 


# REMOVE
thistuple3 = ('apple','banana','cherry')
y3 = list(thistuple3) 
y3.remove('apple') 
thistuple3 = tuple(y3) 

del thistuple3 
print(thistuple3) # will error because it doens't exist anymore 

# UNPACK: like unpack a collection 