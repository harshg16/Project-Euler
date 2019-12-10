n = 600851475143
f = n ** 0.5
l = []
l.append(n)
if n % 2 == 0:
    for x in range(2,int(f)+1,1):
        if n % x == 0:
            l.append(x)
            l.append(n / x)
    
else:
    for x in range(3,int(f)+1,2):
        if n % x == 0:
            l.append(x)
            l.append(n / x)
l.sort()
pr = []

def is_prime(num):
    factor = 3
    while (factor <= num**0.5):
        if num%factor == 0:
             return False
        factor +=2
    return True

for x in l:
    if is_prime(x):
        pr.append(x)
        
if int(f)**2 == n:
    print (len(l) - 1)
else:
    print (len(l))
    
print(pr)