x = input()
y = input()
z = input()
chars = {}

for char in x:
    chars[char] = chars.get(char, 0) + 1

for char in y:
    chars[char] = chars.get(char, 0) + 1

for char in z:
    if chars.get(char, 0) == 0:
        print("NO")
        break
    chars[char] -= 1
else:
    for char in chars:
        if chars[char] != 0:
            print("NO")
            break
    else:
        print("YES")
