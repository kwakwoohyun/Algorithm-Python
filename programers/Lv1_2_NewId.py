def solution(new_id):
    answer = ''
    answer = new_id.lower()
    for i in answer:
        if not i.isdigit() and not i.islower() and not i == '-' and not i == '_' and not i == '.':
            answer = answer.replace(i, "")
    while answer.find('..') != -1:
        answer = answer.replace('..', '.')
    answer = answer.strip('.')
    if answer == '':
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[0:15]
        if answer.strip()[-1] == '.':
            answer = answer.strip('.')
    while len(answer) <= 2:
        answer = answer + answer.strip()[-1]
    return answer
