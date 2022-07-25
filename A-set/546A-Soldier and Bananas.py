# 546A | Soldier and Bananas

k, n, w = list(map(int, input().split()))

for i in range(1, w+1):
    n -= (i * k)

print(0) if n >= 0 else print(abs(n))
