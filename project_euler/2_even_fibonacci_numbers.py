rtn = 0
a = 0
b = 1
c = a+b
while c < 4e6:
    if c % 2 == 0:
        rtn += c
    a = b
    b = c
    c = a + b
print(rtn)