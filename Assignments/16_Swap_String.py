string = "Abhiskeh"
print(string)

chars = list(string)
chars[5], chars[7] = chars[7], chars[5]
string = "".join(chars)

print(string)
