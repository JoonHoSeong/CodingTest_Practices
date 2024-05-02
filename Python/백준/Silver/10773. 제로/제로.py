temp = []
answer = []
for i in range(int(input())) :
    temp.append(int(input()))
for i in temp :
    if i == 0 :
        answer.pop()
    else :
        answer.append(i)
print(sum(answer))