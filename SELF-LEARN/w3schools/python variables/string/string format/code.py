# In Python, we cannot combine strings and numbers like this
age = 36
txt = 'My age is: ' + age 
print(txt) 

'''
→ use f-strings or `format()` -> adding `f` before the string and the placeholders `{}` containing the variables and other operations 
can modify in the placeholders with modifiers `:` , followed by a legal formatting type like `.2f` (fixed point number with 2 decimals)
'''

# Placholders can also contain Python code, like math operations 
price = 69
txt = f'My price is: {price:.2f} dollars'
print(txt) 

txt1 = f'The price is {20*59} dollars'
print(txt1) 

price2 = 59 
tax = 0.25 
txt3 = f'The price is {price2 + (price2 * tax)} dollars'
print(txt3) 

fruits = 'apples'
txt4 = f'I love {fruits.upper()}'
print(txt4) 

price = 59000
txt5 = f'The price is {price:,} dollars'
# the ',' is the thousand separator
print(txt5) 

    # can also define the function 
def my_converter(x):
	return x * 0.3048 

txt6 = f'The plane is flying at a {my_converter(30000)} meter latitude'
print(txt6) 