s1 = 0
s2 = 0
for x in range (1,101):
    s1 += x**2
    s2 += x
s2 = s2 **2
print(s2-s1)