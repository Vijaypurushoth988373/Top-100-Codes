# Check if a Number is Positive and Negative in Python

#For Instance,
#Input : num = 20
#Output : The number is Positive.

# Method - 1 ---> Brute Force

num=15
if num>0:
    print('Positive')
elif num<0:
    print('Negative')
else:
    print('Zero')

# Method - 2 ---> Using Nested If - Else Statements

num=15
if num>0:
    if num==0:
        print('Zero')
    else:
        print('Positive')
else:
    print('Negative')

# Method - 3 ---> Using Ternary Operator

num=15
print('Positive' if num>0 else 'Negative')
