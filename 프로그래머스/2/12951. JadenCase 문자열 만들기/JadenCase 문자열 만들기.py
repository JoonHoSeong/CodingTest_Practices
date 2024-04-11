def solution(s):
    answer = []
    s = s.lower()
    s = s.split(' ')
    for i in range(len(s)) :
        if not s[i] :
            answer.append('')
        else :
            answer.append(s[i][0].upper() + s[i][1:])
            
    return ' '.join(answer)