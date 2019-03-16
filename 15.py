def mix(s1, s2):
    s1_all = ''.join(s1.translate(str.maketrans(',.?:/;', '      ')).split(' '))
    s2_all = ''.join(s2.translate(str.maketrans(',.?:/;', '      ')).split(' '))
    s1_lower = ''.join(s1.lower().translate(str.maketrans(',.?:/;', '      ')).split(' '))
    s2_lower = ''.join(s2.lower().translate(str.maketrans(',.?:/;', '      ')).split(' '))
    set1 = set(s1_all) & set(s1_lower)
    set2 = set(s2_all) & set(s2_lower)

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
