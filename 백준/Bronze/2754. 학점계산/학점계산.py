score = input()
answer = 0.0
if score[0] == 'A' :
    answer+=4
elif score[0] == 'B' :
    answer+=3
elif score[0] == 'C' :
    answer+=2
elif score[0] == 'D' :
    answer+=1
try :
    if score[1] == '+' :
        answer+= 0.3
    elif score[1] =='-' :
        answer-= 0.3
except :
    pass
print(answer)