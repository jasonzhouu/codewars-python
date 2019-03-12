def remove_exclamation_marks(s):
    s = list(s)
    for x in s:
        if x == "!":
            s.remove(x)
    return "".join(s)


s = "hello!"
print(remove_exclamation_marks(s))
