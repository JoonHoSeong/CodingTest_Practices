import copy

def solution(arr):
    answer = 0
    temp = []
    while temp != arr :
        temp = copy.deepcopy(arr)
        for i in range(len(arr)) :
            if arr[i]%2==0 and arr[i]>=50 :
                arr[i] //= 2
            elif arr[i]%2!=0 and arr[i]<50 :
                arr[i] = arr[i]*2+1
        answer += 1
    return answer-1