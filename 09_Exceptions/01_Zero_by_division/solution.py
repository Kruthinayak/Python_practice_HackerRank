# HackerRank: Exceptions
# Practice with try-except and handling errors

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):

    try:
        # Read two values and convert them to integers
        a, b = map(int, input().split())

        # Perform integer division
        print(a // b)

    except ZeroDivisionError:
        # This error occurs when b is 0
        print("Error Code: integer division or modulo by zero")

    except ValueError as e:
        # This error occurs when a or b cannot be converted to an integer
        print("Error Code:", e)