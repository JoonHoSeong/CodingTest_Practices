def solution(n):
    answer = []
    while True :
        answer.append(n)
        if n%2 == 0 :
            n = n/2
        else :
            n = 3*n +1
        if n == 1 :
            answer.append(n)
            break
        
    return answer