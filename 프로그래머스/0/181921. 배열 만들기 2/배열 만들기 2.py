def solution(l, r):
    answer = []
    for i in range(l,r+1) :
        temp = str(i).replace('5', '').replace('0', '')
        if temp == '' :
            answer.append(i)
    if answer == [] :
        return [-1]
    return answer