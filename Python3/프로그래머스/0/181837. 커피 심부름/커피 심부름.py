def solution(order):
    answer = 0
    ame = 0
    late = 0
    for o in order :
        if 'americano' in o :
            ame += 1
        elif 'cafelatte' in o :
            late += 1
        else :
            ame += 1
    answer = 4500 * ame + 5000*late
    return answer