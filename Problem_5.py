sources = {2:0,
           3:0,
           5:0,
           7:0,
           11:0,
           13:0,
           17:0,
           19:0}

factors = [2,3,5,7,11,13,17,19]
for x in range (2,21):
    for y in factors:
        count = 0
        while(x%y == 0 and x > 1):
            count += 1
            x = x/y
        
        if(sources[y] < count):
            sources[y] = count

print(sources)
prod = 1

for x in factors:
    if(sources[x] != 0):
        prod *= x ** sources[x]

print(prod)    