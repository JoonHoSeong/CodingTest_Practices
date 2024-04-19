def solution(code):
    answer = ''
    mode = True
    for i,c in enumerate(code) :
        if c == '1' :
            mode = not mode
            continue
        if mode :
            if i%2 == 0 :
                answer+= c
        else :
            if i%2 == 1 :
                answer += c
    if answer == '' :
        return "EMPTY"
    return answer