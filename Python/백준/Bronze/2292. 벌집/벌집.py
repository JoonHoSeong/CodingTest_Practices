num = int(input())
temp = 1
cnt = 0
while True :
     temp = temp + (cnt*6)
     if temp >= num :
         break
     cnt += 1
print(cnt+1)