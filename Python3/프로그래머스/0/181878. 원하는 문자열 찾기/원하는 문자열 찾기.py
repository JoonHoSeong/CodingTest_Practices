def solution(myString, pat):
    myString = myString.lower()
    if pat.lower() in myString :
        return 1
    return 0