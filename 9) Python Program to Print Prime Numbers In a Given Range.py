# Python Program to Print Prime Numbers In a Given Range

# Example
# Input : low = 2 , high = 10
# Output : 2 3 5 7

# Prime Numbers
# A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. A natural number greater than 1 that is not prime is called a composite number. For example, 5 is prime because the only ways of writing it as a product, 
# 1 × 5 or 5 × 1, involve 5 itself.

# Method 1: Using inner loop Range as [2, number-1]

low, high = 2, 10
primes = []

for i in range(low, high + 1):
    flag = 0
    if i < 2:
        continue
    if i == 2:
        primes.append(2)
        continue

    for x in range(2, i):
        if i % x == 0:
            flag = 1
            break

    if flag == 0:
        primes.append(i)

print(primes)