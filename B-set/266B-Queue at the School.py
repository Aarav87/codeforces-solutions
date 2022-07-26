# 266B | Queue at the School

n, t = list(map(int, input().split()))
queue = input()

for _ in range(t):
    i = 0
    while i < n:
        if queue[i:i+2] == "BG":
            queue = queue[:i] + "GB" + queue[i+2:]
            i += 1
        i += 1
print(queue)
