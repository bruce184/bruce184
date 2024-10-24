'''
    to store **multiple items in 1 variable** 
    use `[]`
    list items are **ordered (indexed)**, **changable**, and **allow duplicate values** 
    there can be many different data types in a list 
    use `in` to locate a variable
'''

# Create
list1 = ['apple','banana','cherry','mango']
thislist = list(('apple','banana','cherry')) # use constructor 
print(list1)

# Duplication 
list2 = ['apple','banana','cherry','cherry']
print(list2)

# length 
list3 = ['apple','banana','cherry']
print(len(list3))

# different 
list4 = ['abc',34,True]

# type 
print(type(list1))
print(type(list2))
print(type(list3))
print(type(list4))