def swap_case(s):
    result = ""

    for ch in s:
        if ch.isupper():
            result = result + ch.lower()

        elif ch.islower():
            result = result + ch.upper()

        else:
            result = result + ch

    return result