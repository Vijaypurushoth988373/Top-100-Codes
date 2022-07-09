# Check Whether a Number is a Prime or Not in Python

# Example
# Input : 11
# Output : 11 is a Prime

# Method 1: Simple iterative solution

num = 15
flag = 0
for i in range(2, num+1):
    if num%i==0:
        flag = 1
        break
if flag == 1:
    print('Not Prime')
else:
    print('Prime')

# Method 2: Optimization by break condition

num = 15
flag = 0
if num < 2:
    flag = 1
else:
    for i in range(2, num+1):
        if num%i==0:
            flag = 1
            break
if flag == 1:
    print('Not Prime')
else:
    print('Prime')

# Method 3: Optimization by n/2 iterations

num = 15
flag = 0
if num <2:
    flag = 1
else:
    for i in range(2, int((num/2)+1)):
        if num % i == 0:
            flag = 1
            break
if flag == 1:
    print('Not Prime')
else:
    print('Prime')