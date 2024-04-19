def solution(date1, date2):
    if int(''.join(list(map(str,date1)))) < int(''.join(list(map(str,date2)))) :
        return 1
    return 0