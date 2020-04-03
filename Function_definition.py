#!/usr/bin/python"

def f(x):
    return(x*x)
print(f(3))

def f(a,b):
    print('You called f(a,b) with the value a = ' + str(a) + ' and b = ' + str(b))
    print('a * b = ' + str(a*b))
f(4,2)
