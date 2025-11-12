'''Sometimes we want to perform actions that are not built into Python.

Then we can create our own algorithms.

For example, an algorithm can be used to find the lowest value in a list, like in the example below:

'''

#Create an algorithm to find the lowest value in a list:

x=[5,6,4,8,2,9,7,0]
min_value=x[0]
for i in x:
    if i < min_value:
        min_value=i
print("lowest Value is:",min_value)


"""The algorithm above is very simple, and fast enough for small data sets, but if the data is big enough, any algorithm will take time to run.

This is where optimization comes in.

Optimization is an important part of algorithm development, and of course, an important part of DSA programming.

"""