#!/usr/bin/python
x = 13
if x < 10:
    print("x smaller than 10")
else:
    print("x is bigger than 10 or equal")

age = 27
print("Enter your age")
guess = int(input("Guess: "))
if guess > 10 and guess < 20:
    print("In range")
else:
    print("Out of range")
