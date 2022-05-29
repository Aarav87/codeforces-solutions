# 996A | Hit the Lottery

money = int(input())
bills = [100, 20, 10, 5, 1]

min_bills = 0
for bill in bills:
    num_of_bill = money//bill
    if num_of_bill >= 1:
        min_bills += num_of_bill
        money -= num_of_bill*bill

print(min_bills)