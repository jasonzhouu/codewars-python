def mix(s1, s2):
    dic = {}
    for i in range(97, 123):
        i = chr(i)
        val1, val2 = s1.count(i), s2.count(i)
        dic[i] = {
            'max': max(val1, val2),
            'winner': '1' if val1 > val2 else '2' if val1 < val2 else '='
        }

    li = []
    for i in dic:
        li.append({
            'letter': i,
            'max': dic[i]['max'],
            'winner': dic[i]['winner'],
            'weight': 0
        })
    weight_of_winner = {
        "1": 3,
        "2": 2,
        "=": 1
    }
    for i in li:
        i['weight'] += i['max']
        i['weight'] += 0.1 * weight_of_winner[i['winner']]
        i['weight'] += 0.001 * (200 - ord(i['letter']))

    li = sorted(li, key=lambda x: x['weight'], reverse=True)
    result = ''
    for i in li:
        if i['max'] > 1:
            result += (i['winner'] + ':' + i['letter'] * i['max'] + '/')
    return result.strip('/')
            
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
