s = input()
def check(method):
    found = False

    for ch in s:
        if method(ch):
            found = True
            break

    print(found)


check(str.isalnum)
check(str.isalpha)
check(str.isdigit)
check(str.islower)
check(str.isupper)