# 59A | Word

s = input()

upper = 0
lower = 0
for char in s:
    if char.isupper():
        upper += 1
    else:
        lower += 1

print(s.upper()) if upper > lower else print(s.lower())
