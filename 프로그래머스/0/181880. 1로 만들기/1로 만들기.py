def solution(num_list):
    answer = 0
    for i in num_list :
        div_num = 0
        while True :
            if i%2 == 0 :
                i /= 2
                div_num += 1
            elif i == 1 :
                break
            else :
                i = (i-1)/2
                div_num += 1
        answer += div_num
    return answer