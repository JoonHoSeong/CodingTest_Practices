def solution(n, m):
    answer = []
    i = n
    while(1) :
        if n%i == 0 and m%i == 0 :
            answer.append(i)
            break
        i -= 1
    i = m
    while(1) :
        if i%n == 0 and i%m == 0 :
            answer.append(i)
            return answer
        i += 1