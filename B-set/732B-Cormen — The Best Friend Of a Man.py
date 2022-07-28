# 732B | Cormen — The Best Friend Of a Man

n, k = list(map(int, input().split()))
walks = list(map(int, input().split()))

min_walks = 0
for i in range(1, n):
    if not walks[i - 1] + walks[i] >= k:
        min_walks += k - (walks[i - 1] + walks[i])
        walks[i] += k - (walks[i - 1] + walks[i])

print(min_walks)

for i in range(n):
    if i == n:
        print(walks[i])
    else:
        print(walks[i], end=" ")
