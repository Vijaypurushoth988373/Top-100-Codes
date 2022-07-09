# Check if a Year is a Leap Year or Not in Python

# Example
# Input : 2020
# Output : It's a Leap Year.

# Conditions for a Leap Year
# Here are the two conditions that any year must satisfy to be called a leap year
# 1. The year must be perfectly divisible by 400.
# 2. The number must be divisible by 4 but not by 100.

# Method 1: Using if-else statements 1

year = 2000
if (year%400==0) or (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print('Not a Leap Year')

# Method 2: Using if-else Statements 2

year = 2001
if( ((year % 4 == 0) and (year % 100 != 0)) or (year % 400==0) ):
    print("Leap Year")
else:
    print("Not leap Year")