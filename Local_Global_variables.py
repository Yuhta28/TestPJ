#Local variables
def sum(x,y):
    sum = x + y
    return sum
print(sum(8,6))
# print(x)  # x is not fefined because of local variables

#Global variables
z = 10
def afunction():
    global z
    print(z)
    z =9

afunction()
print(z)

#Exercise
a = 10

def func1():
    global a
    a = 3

def func2(b,c):
    global a
    return a+b+c

print(a)
func1()
total = func2(4,5)
print(a)
print(total)
