def solution(myString):
    answer = sorted(myString.split('x'))
    answer = [i for i in answer if i != '']
    return answer