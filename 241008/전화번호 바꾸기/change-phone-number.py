number = list(input().split("-"))
# print(number)
number[1], number[2] = number[2], number[1]
print("-".join(number))