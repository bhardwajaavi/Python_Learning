#Strings are Arrays
'''Like many other popular programming languages, strings in Python are arrays of unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.'''


a = "Hello, Aavi Bhardwaj!"
print(a[1])
print(a[6])
print(a[9])


#Looping Through a String
'''Since strings are arrays, we can loop through the characters in a string, with a for loop.'''

for x in "Aavi":
  print(x) 


#String Length
'''To get the length of a string, use the len() function.'''


a = "Hello, Aavi Bhardwaj!"
print(len(a))


#Check String
'''To check if a certain phrase or character is present in a string, we can use the keyword in.'''

txt = "My name is Aavi Bhardwaj!"
print("Aavi" in txt)


#Print only if "free" is present:

txt = "My name is Aavi Bhardwaj!"
if "Aavi" in txt:
  print("Yes, 'Aavi' is present.")
  
  
  
#Check if NOT
'''To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

Example
Check if "Sharma" is NOT present in the following text:'''

txt = "My name is Aavi Bhardwaj!"
print("Sharma" not in txt)