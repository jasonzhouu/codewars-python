def maps(a):
    index = 0
    for value in a:
        a[index] = value * 2
        index += 1
    return a

a = [1, 2, 3]
print(maps(a))
