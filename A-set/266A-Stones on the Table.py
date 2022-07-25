# 266A | Stones on the Table

n = int(input())
s = input()

remove = 0
for i in range(1, n):
    if s[i] == s[i-1]:
        remove += 1

print(remove)
