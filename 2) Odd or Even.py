# Check Whether a Number is Even or Odd in Python

#For Instance,
#Input : num = 20
#Output : The number is Even.

# Method 1 : Using Brute Force

num=int(input('Enter a Number : '))
if num % 2 == 0:
    print('The number is Even')
else:
    print('The number is Odd')

# Method 2 : Using Ternary Operator

#Ternary Operator Syntax Python
#( True : Action ) if ( Condition ) else ( False : Action )

num = 18
print('Even') if num%2==0 else print('Odd')

#Method 3 : Using Bitwise Operator

def isEven(num):
    return not num&1

if __name__ == '__main__':
    num = 13
    if isEven(num):
        print('Even')
    else:
        print('Odd')
