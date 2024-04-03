def solution(num_list):
    even_sum = 0
    odd_sum = 0
    for i in range(len(num_list)) :
        if (i+1)%2 == 0 :
            even_sum += num_list[i]
        else :
            odd_sum += num_list[i]
    if even_sum > odd_sum :
        return even_sum
    return odd_sum