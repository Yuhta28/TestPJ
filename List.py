#!/usr/bin/python
l = ["Drake", "Derp", "Derek", "Dominuque"]
print(l)    # prints all elements
print(l[0]) # prints first element
print(l[1]) # prints second element

# Add/remove
print(l)
l.append("Victoria")    # add element
print(l)
l.remove("Derp")        # remove element
print(l)
l.remove("Drake")
print(l)

#Sort list
l.append("Ace")
print(l)
l.sort()    # sorts the list in plphabetical order
print(l)
l.reverse() # reverse order
print(l)