thislist = ['apple','banana','cherry']
thislist [1:3] = ['watermelon','blackcurrant'] # insert more items 
thislist [1:3] = ['pinapple']                  # insert less items 

# ADD
    # Insert: at a specific index (must be 2 arguments) 
thislist.insert(2, 'watermelon')
print(thislist)

    # Append: at the end of a list; if append a collection, it will its parentheless  
thislist.append('orange')
print(thislist)

    # Extend: to append (at the end) from another collections (list, tuple, set, dictionary,...)
tropical = ['mango','pineapple','papaya']
thislist.extend(tropical)
print(thislist)

# REMOVE 
    # Remove: a specific ITEM, or the first occurrence of that item
thislist1 = ["apple", "banana", "cherry"]
thislist2 = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

    # Pop: a specific INDEX or the last item (no index)
thislist3 = ["apple", "banana", "cherry"]
thislist3.pop(1)
print(thislist3)
thislist4 = ["apple", "banana", "cherry"]
thislist4.pop()
print(thislist4)

    # Delete: a specific INDEX or all of it (no index)

    # Clear: empty the ITEMS, the collection remains
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

