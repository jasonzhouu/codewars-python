def solution(string):
    li = list(string)
    li2 = []
    for i in range(len(li)):
        li2.append(li[len(li)-i-1])
    return "".join(li2)

print(solution("hello"))
