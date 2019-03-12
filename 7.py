def repeat_str(string, repeat):
    solution = ''
    for i in range(repeat):
        solution += string
    return solution

print(repeat_str("hello ", 5))
