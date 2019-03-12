def correct(string):
    return string.translate(str.maketrans("501", "SOI"))

print(correct("NEWY0RK"))
