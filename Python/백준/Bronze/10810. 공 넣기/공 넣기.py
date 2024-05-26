num, iter_num = map(int,input().split(' '))
answer = [0 for _ in range(num)]
for i in range(iter_num):
    a,b,v = map(int,input().split(' '))
    for j in range(a-1,b) :
        answer[j] = v
answer = map(str, answer)
print(' '.join(answer))