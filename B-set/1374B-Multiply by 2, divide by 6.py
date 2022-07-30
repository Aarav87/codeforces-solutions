# 1374B | Multiply by 2, divide by 6

t = int(input())

for _ in range(t):
    n = int(input())
    moves = 0

    while n != 1:
        if n % 3 != 0:
            moves = -1
            break

        if n % 6 == 0:
            n //= 6
        else:
            n *= 2

        moves += 1

    print(moves)