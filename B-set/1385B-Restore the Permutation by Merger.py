# 1385B | Beautiful Restore the Permutation by Merger

t = int(input())

for _ in range(t):
    n = int(input())
    p = input().split()
    visited = set()

    for num in p:
        if num not in visited:
            visited.add(num)

            if len(visited) == n:
                print(num)
            else:
                print(num, end=" ")
