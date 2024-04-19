def solution(my_string, queries):
    my_string = list(my_string)
    for i in queries :
        my_string[i[0]:i[1]+1] = list(reversed(my_string[i[0]:i[1]+1]))
    return ''.join(my_string)