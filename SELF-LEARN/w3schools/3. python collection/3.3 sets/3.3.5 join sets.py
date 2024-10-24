'''
    The union() and update() methods joins all items from both sets, 
    EXCEPT the duplicate
'''
set1 = {'a','b','c'}
set2 = {1,2,3}

# Use union() 
set3 = set1.union(set2)
print(set3)

# Use update()
set1.update(set2)
print(set1)

    # 2nd method 
set3 = set1 | set2
print(set3)

# Multiple Sets
set5 = {'a','b','c'}
set6 = {1,2,3}
set7 = {'John','Elena'}
set8 = {'apple','banana','cherry'}
myset = set1.union(set5,set6,set7)
print(myset)

# With other collection types 
x = {'a','b','c'}
y = (1,2,3) 

z = x.union(y)
print(z)

# Use intersection(): method keeps ONLY the duplicates.
set9 = {'apple','banana','cherry'}
set10 = {'google','mircrosoft','apple'}

set11 = set9.intersection(set10)
print(set11) 
set11 = set9 & set10 # 2nd method

# Use difference(): keeps the items from the first set that are not in the other set(s).
set12 = {'apple','banana','cherry'}
set13 = {'google','microsoft','apple'}

set14 = set12.difference(set12)
set14 = set12 - set13 # 2nd method 
print(set14) 
     
     #symmetric_difference() method keeps all items EXCEPT the duplicates 
     # (NOT present in BOTH sets)
set15 = {'apple','banana','cherry'}
set16 = {'google','microsoft','apple'}

set17 = set15.symmetric_difference(set16) 
set17 = set15 ^ set16
print(set3) 
    # symmetric_difference_update() like intersection()
set18 = {'apple','banana','cherry'}
set19 = {'google','mircrosoft','apple'}

set18.symmetric_difference_update(set19)
print(set1) 