s = input()

result = ""
capitalize_next = True

for ch in s:
    if capitalize_next and ch.isalnum():
        result += ch.upper()
        capitalize_next = False
    else:
        result += ch

    if ch == " ":
        capitalize_next = True

print(result)