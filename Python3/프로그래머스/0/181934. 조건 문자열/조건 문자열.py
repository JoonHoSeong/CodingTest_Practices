def solution(ineq, eq, n, m):
    qurey = ''
    if eq != '!' :
        qurey = ineq+eq
    else:
        qurey = ineq
    if eval(str(n)+qurey+str(m)) :
        return 1
    return 0