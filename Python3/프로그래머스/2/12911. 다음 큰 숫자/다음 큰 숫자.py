def solution(n):
    bin_n = str(bin(n)[2:])
    n2 = n+1
    while bin_n.count('1') != str(bin(n2)[2:]).count('1') :
        n2 += 1
    return n2