is_isogram = lambda string: len(string) == len(set(string.lower()))

print(is_isogram("mqizrzax"))
print(is_isogram("helo"))
