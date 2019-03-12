def remove_exclamation_marks(s):
    s2 = ''
    for i in s:
        if i != '!':
            s2 += i
    return s2

s = "hello!"
print(remove_exclamation_marks(s))
