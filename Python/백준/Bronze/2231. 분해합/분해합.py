num = input()
answer = 0
for i in range(1,int(num)) :
    if sum(list(map(int,list(str(i))))) + i == int(num) :
        answer = i
        break
        
print(answer)