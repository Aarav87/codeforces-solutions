# 271A | Beautiful Year

y = int(input())

while True:
    y += 1
    if len(set(str(y))) == len(str(y)):
        break

print(y)
