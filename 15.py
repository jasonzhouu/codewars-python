def mix(s1, s2):
    s1 = ''.join(s1.lower().translate(str.maketrans(',.?:/;', '      ')).split(' '))
    s2 = ''.join(s2.lower().translate(str.maketrans(',.?:/;', '      ')).split(' '))
    set1 = set(s1)
    set2 = set(s2)

    dic = {}
    for i in set1:
        dic[i] = {
            's1': s1.count(i),
            's2': 0,
            'max': s1.count(i),
            'winner': '1'
        }
    for i in set2:
        s1_temp = dic[i]['s1'] if i in dic else 0
        dic[i] = {
            's1': s1_temp,
            's2': s2.count(i),
            'max': max(s1_temp, s2.count(i)),
        }
        if dic[i]['s1'] > dic[i]['s2']:
            dic[i]['winner'] = '1'
        elif dic[i]['s1'] < dic[i]['s2']:
            dic[i]['winner'] = '2'
        else:
            dic[i]['winner'] = '='

    li = []
    for i in dic:
        li.append({
            'letter': i,
            'max': dic[i]['max'],
            'winner': dic[i]['winner']
        })

    li = sorted(li, key=lambda x: x['max'], reverse=True)
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
