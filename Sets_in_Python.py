# Set example

x = set(["Posted", "Radio", "Telegram", "Radio"]) # A set may not contain the same element multiple times.
print(x)

# Set Method
# Clear elements
y = set(["Posted", "Rao", "Teram", "Rdio"])
y.clear()
print(y)
# Add elements
z = set(["Posted", "Rao", "Teram", "Rdio"])
z.add("AAQWER")
print(z)
# Remove elements
p = set(["Posted", "Rao", "Teram", "Rdio"])
p.remove("Posted")
print(p)
# Difference between two sets
q = set(["Aka", "Midori", "Shiro", "Kuro"])
r = set(["Ao", "Momo", "Murasaki", "Kuro"])
print(q.difference(r))
print(r.difference(q))

print("")
# Subset
m = set(["a","b","c","d"])
n = set(["c","d"])
print(m.intersection(n))