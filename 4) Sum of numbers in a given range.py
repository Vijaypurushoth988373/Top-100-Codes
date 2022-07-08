# Find the Sum of Numbers in a given Range in Python

# Example
# Input : 2 5
# Output : 14

# Method 1: Using Brute Force

from __future__ import print_function


num1, num2 = 3, 6
sum = 0
for i in range(num1, num2+1):
    sum+=i
print(sum)

# Method 2: Using the Formula

# The formula to find Sum of Numbers in a given Range is:
# Sum = b * ( b + 1 ) / 2 – a * ( a + 1 ) / 2 + a .

a, b = 3, 6
print(b * ( b + 1) / 2 - a * ( a + 1) / 2 + a) 

# Method 3: Using Recursion

def sumofNum(sum, num1, num2):
    if num1 > num2:
        return sum
    return num1 + sumofNum(sum, num1+1, num2)

num1, num2 = 3, 6
sum = 0
print(sumofNum(sum, num1, num2))