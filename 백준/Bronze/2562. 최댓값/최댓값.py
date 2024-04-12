temp = []
for i in range(9) :
    temp.append(int(input()))
print(max(temp))
print(temp.index(max(temp))+1)