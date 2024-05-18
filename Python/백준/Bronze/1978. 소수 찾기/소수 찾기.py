_ = input()
nums = list(map(int, input().split(' ')))
answer = 0
for n in nums :
    temp = 0
    for i in range(n) :
        if n%(i+1) == 0 :
            temp += 1
    if temp == 2 :
        answer += 1
print(answer)