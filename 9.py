def is_isogram(string):
    li = sorted(string.lower())
    for i in range(len(li)-1):
        if li[i] == li[i+1]:
            return False
    return True

print(is_isogram("mqizrzax"))
