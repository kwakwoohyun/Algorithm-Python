def solution(s):
    answer = ''
    num_dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                'eight': '8', 'nine': '9'}
    word = ''
    for i in s:
        if i.isalpha():
            word = word + i
            if word in num_dict:
                answer = answer + num_dict[word]
                word = ''
        else:
            answer = answer + i
    return int(answer)
