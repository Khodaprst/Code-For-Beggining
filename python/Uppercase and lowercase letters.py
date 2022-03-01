my_string = input()
lowers = []
uppers = []
for character in my_string:
    if character.islower():
        lowers.append(character)
    elif character.isupper():
        uppers.append(character)

if len(uppers) <= len(lowers):
    print(my_string.lower())

elif len(uppers) > len(lowers):
    print(my_string.upper())