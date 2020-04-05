from functools import reduce

f = lambda x : x > 10
print(f(2))
print(f(12))

list = [1,8,3,4,5]
s = reduce(lambda y,z: y if (y > z) else z, list)
print(s)