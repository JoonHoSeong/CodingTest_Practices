def solution(binomial):
    binomial =binomial.split(' ')
    if binomial[1] == '+' :
        return int(binomial[0]) + int(binomial[2])
    elif binomial[1] == '-' :
        return int(binomial[0]) - int(binomial[2])
    elif binomial[1] == '*' :
        return int(binomial[0]) * int(binomial[2])