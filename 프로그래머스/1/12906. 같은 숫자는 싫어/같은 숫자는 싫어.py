def solution(arr):
    answer = []
    temp = -1
    for i in arr :
        if temp == i :
            pass
        else :
            answer.append(i)
        temp = i
    return answer