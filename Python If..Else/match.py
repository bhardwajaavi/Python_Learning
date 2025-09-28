#The Python Match Statement
'''Instead of writing many if..else statements, you can use the match statement.
The match statement selects one of many code blocks to be executed.



Syntax
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
    
    
This is how it works:

The match expression is evaluated once.
The value of the expression is compared with the values of each case.
If there is a match, the associated block of code is executed.
The example below uses the weekday number to print the weekday name:'''


day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
    
    
    
    
#Default Value
'''Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:

Example'''

day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
    
    
    
    
    

