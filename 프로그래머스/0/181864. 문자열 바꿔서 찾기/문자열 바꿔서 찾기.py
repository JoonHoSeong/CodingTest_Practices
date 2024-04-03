def solution(myString, pat):
    temp = ''
    for i in pat :
        if i =='A' :
            temp += 'B'
        else :
            temp += 'A'
    if temp in myString :
        return 1
    return 0