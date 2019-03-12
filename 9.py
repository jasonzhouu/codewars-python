def is_isogram(string):
    string = string.lower()
    for i in string:
        if string.count(i) > 1:
            return False
    return True

print(is_isogram("mqizrzax"))
print(is_isogram("helo"))
