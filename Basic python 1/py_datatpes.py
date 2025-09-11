#datatypes
"""Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType"""


#Getting the Data Type
"""You can get the data type of any object by using the type() function:"""

x="Hello aavi"
print(type(x))

x = ["apple", "banana", "cherry"]
print(type(x))

x = b"Hello"
print(type(x))

x = bytearray(5)
print(type(x))












#Setting the Specific Data Type
"""If you want to specify the data type, you can use the following constructor functions:"""


x = str("Hello World")

#display x:
print(x)

#display the data type of x:
print(type(x)) 
