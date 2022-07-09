# Find the Greatest of the Two Numbers

# Example
# Input : 20 40
# Output : 40

# Method 1: Using if-else Statements

num1, num2 = 20, 40
if num1>num2:
    print(num1)
else:
    print(num2)

# Method 2: Using Ternary Operator

num1, num2 = 20, 40
print((num1 if num1 > num2 else num2))

# Method 3: Using inbuilt max() Function

num1, num2 = 20, 40
print(max(num1, num2))