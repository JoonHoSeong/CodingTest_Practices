def solution(strArr):
    answer = []
    for s in strArr :
        if len(s) > len(answer) :
            while len(s) != len(answer) :
                answer.append(0)

        answer[len(s)-1] += 1
    return max(answer)