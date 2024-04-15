answer = []
for i in range(10) :
    temp = int(input())%42
    if temp not in answer :
        answer.append(temp)
print(len(answer))