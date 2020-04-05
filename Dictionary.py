#!/usr/bin/python

words = {}
words["Hello"]  =   "Bojour"
words["Yes"]    =   "Oui"
words["No"]     =   "Non"
words["Bye"]    =   "Au Revoir"

print(words["Hello"])
print(words["No"])
print(words["Bye"])

dict = {}
dict['Ford']    =   "Car"
dict['Python']  =   "The Python Programming Langueage"
dict[2]         =   "This sentence is stored here"

print(dict['Ford'])
print(dict['Python'])
print(dict[2])

print(words)
del words["Yes"]
print((words))
words["Yes"]    =   "Out"
print((words))