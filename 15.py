def mix(s1, s2):
    dic = {}
    for i in range(97, 123):
        i = chr(i)
        val1, val2 = s1.count(i), s2.count(i)
        if max(val1, val2) > 1:
            dic[i] = {
                'max': max(val1, val2),
                'winner': '1' if val1 > val2 else '2' if val1 < val2 else '='
            }

    li = []
    weight_of_winner = {
        "1": 3,
        "2": 2,
        "=": 1
    }
    for i in dic:
        li.append({
            'string': dic[i]['winner'] + ":" + i * dic[i]['max'],
            'weight': dic[i]['max'] + 0.1 * weight_of_winner[dic[i]['winner']] + 0.001 * (200 - ord(i))
        })
    li = sorted(li, key=lambda x: x['weight'], reverse=True)

    return "/".join(i['string'] for i in li)
            
a = [
    ["Are they here", "yes, they are here"],
    ["looping is fun but dangerous", "less dangerous than coding"],
    [" In many languages", " there's a pair of functions"],
    ["Lords of the Fallen", "gamekult"],
    ["codewars", "codewars"],
    ["A generation must confront the looming ", "codewarrs"],
]

for i in a:
    print('result: ', mix(i[0], i[1]), '\n\n')
