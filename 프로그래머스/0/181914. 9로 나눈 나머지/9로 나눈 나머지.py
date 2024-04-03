def solution(number):
    answer = sum(list(map(int,list(number))))%9
    return answer