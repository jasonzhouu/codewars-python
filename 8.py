def solution(string):
    result = ""
    for chr in string:
        result = chr + result
    return result

print(solution("hello"))
