def solution(my_string, m, c):
    answer = ''
    for j in range(0,len(my_string),m) :
        answer+=my_string[j:m*(j+1)][c-1]
    return answer