#F-Strings
'''F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
Example
Create an f-string:'''

age = 24
p = f"My name is Aavi Bhardwaj I am {age}"
print(p)


#Placeholders and Modifiers
'''A placeholder can contain variables, operations, functions, and modifiers to format the value.
Example
Add a placeholder for the price variable:'''

price = 2000
txt = f"The price is {price} Ruppes"
print(txt)


#A placeholder can include a modifier to format the value.
'''A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
Example
Display the price with 2 decimals:'''

price = 200
txt = f"The price is {price:.2f} Rupees"
print(txt)


#A placeholder can contain Python code, like math operations:
'''Example
Perform a math operation in the placeholder, and return the result:'''

txt = f"The price is {20 * 59} Ruppes"
print(txt)