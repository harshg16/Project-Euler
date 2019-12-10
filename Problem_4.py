def palindrome(x):
    x = str(x)
    rev = x[::-1]
    if (x == rev):
        return True
    else:
        return False

maxi = 0
a = 0
b = 0
for x in range (1000, 10000, 1):
    for y in range (x, 10000, 1):
        if palindrome(x*y) and x*y > maxi:
            maxi = x*y
            a = x
            b = y
            

print(maxi,a,b)
