# 231A | Team

n = int(input())
problems = []

for i in range(n):
    problems.append(list(map(int, input().split())))

implement = 0
for problem in problems:
    teammate_know = 0
    for teammate in problem:
        if teammate == 1:
            teammate_know += 1

    if teammate_know > 1:
        implement += 1

print(implement)