rtn = 0
for n in range(3, 1000, 3):
    rtn += n
for n in range(5, 1000, 5):
    if n % 3 != 0:
        rtn += n
print(rtn)
