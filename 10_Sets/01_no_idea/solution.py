# HackerRank: No Idea!
# Topic: Sets
# Concepts: set(), membership checking, loops, if-elif

# Read n and m
n, m = map(int, input().split())

# Read the array
arr = list(map(int, input().split()))

# Set of numbers we like
A = set(map(int, input().split()))

# Set of numbers we dislike
B = set(map(int, input().split()))

# Start with zero happiness
happiness = 0

# Go through each number in the array
for num in arr:

    # Number is in A → gain happiness
    if num in A:
        happiness += 1

    # Number is in B → lose happiness
    elif num in B:
        happiness -= 1

    # Otherwise → happiness stays unchanged

# Display final happiness
print(happiness)