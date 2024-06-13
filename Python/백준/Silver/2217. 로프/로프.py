lope_list = []
n = int(input())
for _ in range(n) :
    lope_list.append(int(input()))
lope_list.sort()
answer = []
for i,j in enumerate(lope_list) :
    answer.append(j*(n-i))
print(max(answer))