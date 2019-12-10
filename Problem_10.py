sum = 2

def is_prime(num):
    factor = 3
    while (factor <= num**0.5):
        if num%factor == 0:
             return False
        factor +=2
    return True

for x in range (3,2000000,2):
    if is_prime(x):
        sum += x

print(sum)