def print_rangoli(size):
    width = 4 * size - 3

    for i in range(size):
        left = ""

        for j in range(i + 1):
            left += chr(97 + size - 1 - j) + "-"

        left = left[:-1]
        row = left + left[::-1][1:]

        print(row.center(width, "-"))

    for i in range(size - 2, -1, -1):
        left = ""

        for j in range(i + 1):
            left += chr(97 + size - 1 - j) + "-"

        left = left[:-1]
        row = left + left[::-1][1:]

        print(row.center(width, "-"))


size = int(input())
print_rangoli(size)