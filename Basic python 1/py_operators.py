#Python Operators
'''Operators are used to perform operations on variables and values.
In the example below, we use the + operator to add together two values:'''

#Python divides the operators in the following groups:

'''Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators'''

#Python Assignment Operators
'''Assignment operators are used to assign values to variables:'''

x = 5
x += 3
print(x)

x = 5
x%=3
print(x)


#Python Comparison Operators
'''Comparison operators are used to compare two values:'''

x = 5
y = 3

print(x != y)

# returns True because 5 is not equal to 3



x = 5
y = 3

print(x <= y)

# returns False because 5 is neither less than or equal to 3


#Python Logical Operators
'''Logical operators are used to combine conditional statements:


and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)	'''

x = 5

print(x > 3 or x < 4)

# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)


#Python Identity Operators
'''Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator	Description	Example	Try it
is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y	'''

#Python Membership Operators
'''Membership operators are used to test if a sequence is presented in an object:'''


'''in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y	
Python Bitwise Operators
Bitwise operators are used to compare (binary) numbers:'''

#Operator	Name	Description	
'''& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2	'''

#Operator Precedence
'''The precedence order is described in the table below, starting with the highest precedence at the top:

Operator	Description	
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR	
If two operators have the same precedence, the expression is evaluated from left to right.'''

