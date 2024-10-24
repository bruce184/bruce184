# use sort() 
    # alphanumerically
thislist = ['orange','mango','kiwi','pineapple','banana']
thislist.sort()
print(thislist)

    # with conditions
def myfunc(n):
	return abs(n - 50)
	
thislist2 = [100,50,65,82,23]
thislist2.sort(key = myfunc)
print(thislist2) 

    # this function helps with CASE SENSITIVE: 
    # if there is capital letters, lower cases are sorted first
thislist3 = ['banana','Orange','Kiwi','cherry']
thislist3.sort(key = str.lower)
print(thislist3) 

# use reverse()
    # option 1
thislist4 = [100, 50, 65, 82, 23]
thislist4.sort(reverse = True) 
print(thislist4) 

    # option 2 - recommended
thislist5 = ['banana','Orange','Kiwi','cherry']
thislist5.reverse()
print(thislist5) 

marxes = ['Groucho', 'Chico', 'Harpo']


#Sorted: returns a sorted copy of the list
print(sorted(marxes, reverse=False))
 #sort ko phải của (đối tượng) list ở trên
 #là cách thức truyền thống của python lên list
print(marxes)   