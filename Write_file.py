#!/usr/bin/env ptyhon

# Filename to append
filename = "newfile.txt"

# The 'a' flag tells Python to keep the file contents
# and append (add line) at the end of the file.
myfile = open(filename, 'a')

# Add the line
myfile.write('Add to Python\n')

# Close the file
myfile.close()