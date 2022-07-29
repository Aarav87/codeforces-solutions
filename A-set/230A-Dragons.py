# 230A | Dragons

s, n = list(map(int, input().split()))
dragons = []

for _ in range(n):
    x, y = list(map(int, input().split()))
    dragons.append((x, y))

dragons.sort(key=lambda i: i[0])

next_level = True
for dragon in dragons:
    if s > dragon[0]:
        s += dragon[1]
    else:
        next_level = False
        break

print("YES") if next_level else print("NO")
