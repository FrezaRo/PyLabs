list_num = [1, 2, 4, 6, 8, 10, 12, 15, 20, 30]
mult = 1
for i in list_num:
    if i % 3 == 0 and i % 5 == 0:
        mult *= i
print(mult)