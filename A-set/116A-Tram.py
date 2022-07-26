# 116A | Tram

n = int(input())

capacity = 0
passengers = 0
for _ in range(n):
    a, b = list(map(int, input().split()))

    passengers += (b - a)
    if passengers > capacity:
        capacity = passengers

print(capacity)
