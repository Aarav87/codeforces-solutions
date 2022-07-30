# 580A | Kefa and First Steps

n = int(input())
money = list(map(int, input().split()))

if len(money) > 1:
    subsegment = 0
    curr = 1
    for i in range(1, n):
        if money[i] >= money[i - 1]:
            curr += 1
        else:
            curr = 1

        if curr > subsegment:
            subsegment = curr

    print(subsegment)
else:
    print(1)

