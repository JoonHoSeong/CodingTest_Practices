def solution(babbling):
    answer = 0
    speak = ["aya", "ye", "woo", "ma"]
    for b in babbling :
        for s in speak :
            b = b.replace(s, ' ')
        if len(b.replace(' ', ''))==0 :
            answer += 1
    return answer