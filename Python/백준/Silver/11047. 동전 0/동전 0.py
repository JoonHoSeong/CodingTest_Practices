coin_num, total = map(int, input().split(' '))
coin_list = []
for i in range(coin_num) :
    coin_list.append(int(input()))
coin_list.sort(reverse=True)
answer = 0
for c in coin_list :
    if total//c > 0 :
        answer += total//c
        total = total%c
    else : continue
print(answer)