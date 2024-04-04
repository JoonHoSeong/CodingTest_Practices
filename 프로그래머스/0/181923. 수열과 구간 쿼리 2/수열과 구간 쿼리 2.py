def solution(arr, queries):
    answer = []
    for q in queries :
        temp = -1
        min_value = []
        for i in range(q[0],q[1]+1) :
            if arr[i] > q[2] :
                min_value.append(arr[i])
        if min_value != [] :
            answer.append(min(min_value))
        else : answer.append(temp)
    return answer