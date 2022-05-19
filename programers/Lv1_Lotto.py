def solution(lottos, win_nums):
    answer = []
    zero_count = lottos.count(0)
    count = 0
    for i in win_nums:
        if i in lottos:
            count += 1
    answer.append(getRank(count + zero_count))
    answer.append(getRank(count))
    return answer


def getRank(num):
    rank = 0
    if num == 1 or num == 0:
        rank = 6
    elif num == 2:
        rank = 5
    elif num == 3:
        rank = 4
    elif num == 4:
        rank = 3
    elif num == 5:
        rank = 2
    elif num == 6:
        rank = 1
    return rank