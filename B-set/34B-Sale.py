# 34B | Sale

n, m = list(map(int, input().split()))
costs = sorted(map(int, input().split()))

earnings = 0
for i in range(m):
    if costs[i] < 0:
        earnings += costs[i]

print(abs(earnings))
