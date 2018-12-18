def total(initial = 5, *numbers, **keywords):
    count = initial
    for n in numbers:
        count += n
    for key in keywords:
        count += keywords[key]
    return count

print(total(15, 1, 2, 3, k1=10, k2=10))