import math
a, b = map(int, input().split())

sum_prime = 0
min_prime = 10e6

def is_prime(x):
    for i in range(2, int(math.sqrt(x))+ 1):
        if x % i == 0:
            return False
    return True

for num in range(a, b+1):
    if num == 1:
        continue
    if is_prime(num):
        sum_prime += num
        min_prime = min(min_prime, num)

print(sum_prime, end=' ')
print(0 if min_prime == 10e6 else min_prime)