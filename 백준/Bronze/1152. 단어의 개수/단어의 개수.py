words = input().split(' ')
answer = 0
for w in words :
    if w == '' :
        continue
    answer += 1
print(answer)