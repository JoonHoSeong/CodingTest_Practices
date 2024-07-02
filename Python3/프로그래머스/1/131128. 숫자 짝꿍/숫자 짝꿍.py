def solution(X, Y):
    answer = {}
    str_answer = ''
    for i in range(9,-1,-1) :
        a = X.count(str(i))
        b = Y.count(str(i))
        if min(a,b) != 0 :
            answer[str(i)] = min(a,b)
    if list(answer.keys()) == ['0'] :
        return '0'
    if len(answer.keys()) < 1 :
        return '-1'
    for k,v in answer.items() :
        str_answer += k*v
    return str_answer