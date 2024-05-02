num = int(input())
c = 0
a = 1000-num
if a//500 > 0 :
    c += a//500
    a = a%500

if a//100 > 0 :
    c += a//100
    a = a%100

if a//50 > 0 :
    c += a//50
    a = a%50

if a//10 > 0 :
    c += a//10
    a = a%10 

if a//5 > 0 :
    c += a//5
    a = a%5

if a!= 0:
    c += a
    a = 0

print(c)
    