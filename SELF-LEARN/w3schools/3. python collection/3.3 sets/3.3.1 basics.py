'''
    to **store multiple items in a single variable** 
    a collection which is **unordered**, **unchangeable**, **UNINDEXED**, and **NOT allow duplicate values**   ****
        TRUE/1; False/0 are considered the **SAME VALUE***
    set items are **unchangeable**, but we can **remove** and **add new ones** 
    use `{}`
'''

# Many data types 
set1 = {1,5,7,9,3}
set2 = {'apple','banana','cherry'}
set3 = {True, False, True}

# TYPE()
myset = {'apple','banana','cherry'}
print(type(myset))

# SET() CONSTRUCTOR  
thisset1 = set(('apple','banana','cherry')) # note the double round-brackets
print(thisset1)

# LENGTH 
thisset2 = {'apple', 'banana','cherry'}
print(len(thisset2))

# NO DUPLICATION 
thisset3 = {'apple','banana','cherry','cherry','apple'}
print(thisset3) # only cherry will appear 

thisset4 = {'apple','banana','cherry',True, 1,2}
print(thisset4) 