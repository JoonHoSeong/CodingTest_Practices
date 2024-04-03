def solution(arr):
    lenth = len(arr)
    temp = 1
    while True :
        if temp >= lenth :
            break
        temp *= 2
    return arr + [0 for i in range(temp-len(arr))]