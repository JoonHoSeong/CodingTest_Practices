num1, num2 = map(int, input().split())
temp = 0
for i in range(1, num1+1) :
    if num1%i == 0 :
        temp += 1
        if temp == num2 :
            print(i)
            break
if num2 > temp :
    print(0)