# 149A | Business trip

k = int(input())
months = sorted(map(int, input().split()), reverse=True)

if k > sum(months):
    print(-1)
else:
    height = 0
    min_months = 0
    while k > height:
        height += months[min_months]
        min_months += 1

    print(min_months)
