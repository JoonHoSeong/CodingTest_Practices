def solution(my_string, indices):
    indices.sort()
    my_string = list(my_string)
    for i,j in enumerate(indices) :
        del my_string[j-i]
    return ''.join(my_string)