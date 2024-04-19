def solution(my_string, s, e):
    return my_string[:s] + ''.join(reversed(list(my_string)[s:e+1])) + my_string[e+1:]