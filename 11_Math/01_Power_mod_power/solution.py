# Read the first number
a = int(input())

# Read the second number
b = int(input())

# Read the modulus value
m = int(input())

# Calculate a raised to the power b
result1 = pow(a, b)

# Calculate (a raised to the power b) modulo m
result2 = pow(a, b, m)

# Print both results
print(result1)
print(result2)