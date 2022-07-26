# 110A | Nearly Lucky Number

n = input()

lucky_digits = 0
for dig in n:
    if dig == "4" or dig == "7":
        lucky_digits += 1

if lucky_digits == 4 or lucky_digits == 7:
    print("YES")
else:
    print("NO")
