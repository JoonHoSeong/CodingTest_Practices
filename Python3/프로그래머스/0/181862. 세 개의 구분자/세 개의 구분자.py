def solution(myStr):
    answer = []
    for i in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split(' ') :
        if i != '':
            answer.append(i)
    if len(answer) == 0 :
        answer.append("EMPTY")
    return answer