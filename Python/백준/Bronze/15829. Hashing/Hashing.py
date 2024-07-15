num = int(input())
s = list(input())
answer = 0
for i, j in enumerate(s) :
    answer = answer + ((ord(j)-ord('a')+1)*(31**(i)))
print(answer%1234567891)