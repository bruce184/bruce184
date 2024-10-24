'''
    you cannot change its items, but can add new items 
    in a collection, there are ITEMS that have VALUES. 
    For sets, you **CANNOT CHANGE THE VALUE OF THAT ITEM**, but **HAVE TO ADD A WHOLE NEW ONE**
'''

# use add() 
thisset = {'apple','banana','cherry'}
thisset.add('orange')
print(thisset)

# use update()
    # items from another set 
tropical = {'pineapple','mango','papaya'}
thisset.update(tropical)
print(thisset) 

    # a whole other collection 
mylist = ['kiwi', 'orange']
thisset.update(mylist)
print(thisset)
