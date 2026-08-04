def swap_case(s):
    n=int(input())
    result = ""

    for ch in s:
        if ch.isupper():
            result = result + ch.lower()

        elif ch.islower():
            result = result + ch.upper()

        else:
            result = result + ch

    return result