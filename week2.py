import math

# 1c. How many bits are required if you need 18 unique bit strings? Write a short Python function
# that does this calculation for any number of bit strings.
def uniqueBitStrings (n): 
    return math.ceil(math.log2(n))

# Find the ASCII representations of the following using the ASCII chart from the Lecture 2 slides
# and using Python.
def convertToASCII (s):
    return ord(s)

## Convert these binary numbers to base-10. Double check with Python
def convertToBase10 (n):
    return int(n, 2)

## Add these binary numbers. Double check with Python.
def bitAddition(a, b):
    return bin(int(a,2) + int(b,2))

## Convert these binary strings to hexidecimal. Check with Python.
def binaryToHex(b):
    return hex(int(b, 2))