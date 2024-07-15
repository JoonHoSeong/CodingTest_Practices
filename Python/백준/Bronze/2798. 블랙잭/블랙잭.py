num, target = map(int,input().split())
cards = list(map(int,input().split()))
result = []
for i in range(0,len(cards)) :
    for j in range(i+1,len(cards)) :
        for k in range(j+1, len(cards)) :
            temp = cards[i] + cards[j] + cards[k]
            if temp <= target :
                result.append(temp)
print(max(result))