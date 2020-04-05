# Random number between 0 and 1
from random import *
print(random())

# Generate a random number between 1 and 100
from random import *
print(randint(1,100))

x = randint(1,10)
print(x)

# Random floating number between 1 and 10
from random import *
print(uniform(1,10))

# Fun with lists
from random import *
items = [1,2,3,4,5,6,7,8,9]
shuffle(items)
print(items)

x = sample(items,1)     #Choose one number
print(x[0])

y = sample(items,4)     #Choose 4 random number
print(y)

name = ["Alice","Bob","Carter","Dave"]
z = sample(name,1)
print(z[0])

m = sample(name,4)
print(m)