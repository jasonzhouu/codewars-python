def solution(string):
    result = ""
    for i in reversed(string):
        result += i
    return result

print(solution("hello"))
