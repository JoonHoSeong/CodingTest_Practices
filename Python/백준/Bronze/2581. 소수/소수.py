def is_primer(num : int) -> bool :
    if num <= 1 :
        return False
    for j in range(2,int(num**0.5)+1) :
        if num%j == 0 :
            return False
    return True
a = int(input())
b = int(input())
answer = []
for i in range(a,b+1) :
    if is_primer(i) :
        answer.append(i)
if len(answer) < 1 :
    print(-1)
else :
    print(sum(answer))
    print(answer[0])
