# Prints out a few binary numbers.
print(int('00', 2))
print(int('01', 2))
print(int('10', 2))
print(int('11', 2))

# Prints out a few binary numbers.
print(int('00000010', 2))   # outputs 2
print(int('00000011', 2))   # outputs 3
print(int('00010001', 2))   # outputs 17
print(int('11111111', 2))  # outputs 255

inputA = int('0101',2)

print("Before shifting " + str(inputA) + " " + bin(inputA))
print("After shifting in binary: " + bin(inputA << 1))
print("After shifting in decimal: " + str(inputA << 1))

# This code will execute a bitwise logical AND. Both inputA and inputB are bits.
inputA = 1
inputB = 1

print(inputA & inputB)   # Bitwise AND

inputA = int('00100011',2)   # define binary sequence inputA
inputB = int('00101101',2)   # define binary sequence inputB

print(bin(inputA & inputB))   # logical AND on inputA and inputB and output in binary

inputA = int('00100011',2)  # define binary number
inputB = int('00101101',2)  # define binary number

print(bin(inputA))            # prints inputA in binary
print(bin(inputB))            # prints inputB in binary
print(bin(inputA | inputB))   # Execute bitwise logical OR and print result in binary

inputA = int('00100011',2)  # define binary number
inputB = int('00101101',2)  # define binary number

print(bin(inputA))            # prints inputA in binary
print(bin(inputB))            # prints inputB in binary
print(bin(inputA ^ inputB))   # Execute bitwise logical OR and print result in binary