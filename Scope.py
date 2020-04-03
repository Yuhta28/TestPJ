#!/usr/bin/python

def f(x,y,z):
    return x+y+z # this will return the sum because all variables are passed as parameters
sum = f(3,2,1)
print(sum)

#Calling functions in functions
def highFive():
    return 5

def f(x,y):
    z = highFive()  # we get the variable contents from highFive()
    return x+y+z    # return x+y+z. z is reachable because it is defined above
result = f(2,2)
print(result)