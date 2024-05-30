word = input()
answer = len(word)
for i in word :
    if i in 'ABC' :
        answer += 2
    elif i in 'DEF' :
        answer += 3
    elif i in 'GHI' :
        answer += 4
    elif i in 'JKL' :
        answer += 5
    elif i in 'MNO' :
        answer += 6
    elif i in 'PQRS' :
        answer += 7
    elif i in 'TUV' :
        answer += 8
    elif i in 'WXYZ' :
        answer += 9
    else :
        pass
print(answer)