# if the item being removed doesn’t exist, will raise AN ERROR

# use remove()
thisset1 = {'apple','banana','cherry'}
thisset1.remove('banana')
print(thisset1) 

# use discard()
thisset2 = {'apple','banana','cherry'}
thisset2.discard('banana')
print(thisset2) 

# use pop(): will erase an RANDOM ITEM 
thisset3 = {'apple','banana','cherry'}
thisset3.pop()
print(thisset3) 

# use clear(): EMPTY the set 
thisset4 = {'apple','banana','cherry'}
thisset4.clear()
print(thisset4) 

# use delto delete the list completely 
thisset5 = {'apple','banana','cherry'}
del thisset5
print(thisset5) 
