# 160A | Twins

n = int(input())
coins = sorted(map(int, input().split()))[::-1]

min_coins = 0
value = 0
for coin in coins:
    if value > (sum(coins) - value):
        break
    min_coins += 1
    value += coin

print(min_coins)
