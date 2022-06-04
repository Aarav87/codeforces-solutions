# 727A | Transformation: from A to B

a, b = map(int, input().split())

queue = [(a, [a])]
ans = False

while len(queue) > 0:
    num, sequence = queue.pop(0)

    if num == b:
        ans = True
        print("YES\n{}".format(len(sequence)))
        print(*sequence)
        break

    if num * 2 <= b:
        operation1 = sequence.copy()
        operation1.append(num*2)
        queue.append((num*2, operation1))

    if num * 10 + 1 <= b:
        operation2 = sequence.copy()
        operation2.append(num*10+1)
        queue.append((num*10+1, operation2))

if not ans:
    print("NO")