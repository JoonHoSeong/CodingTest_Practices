def solution(brown, yellow):
    answer = [1,1]
    temp = brown+yellow
    while True :
        if answer[0]*answer[1] == temp :
            if (answer[1]-2) * (answer[0]-2) == yellow :
                break
            else :
                answer[1] -= 2
                answer[0] += 2
                continue
        if answer[0]*answer[1] > temp :
            answer[1] -= 1
            answer[0] += 1
            continue
        if answer[0] > answer[1] :
            answer[1] += 1
            continue
        answer[0] += 1
    return answer