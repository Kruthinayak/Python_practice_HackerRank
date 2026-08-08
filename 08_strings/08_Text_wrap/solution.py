def wrap(string, max_width):
    parts = []

    for i in range(0, len(string), max_width):
        parts.append(string[i:i + max_width]) # Append each chunk of the string

    return "\n".join(parts)


string = input() #input of the string
max_width = int(input()) #input of how many characters per line

print(wrap(string, max_width))