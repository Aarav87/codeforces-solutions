# 266A | Stones on the Table

n = int(input())
s = input()

remove = 0
i = 1
while i < n:
    if s[i] == s[i-1]:
        remove += 1
    i += 1

print(remove)
