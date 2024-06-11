for _ in range(int(input())) :
    num = int(input())
    a, b, c, d = 0, 0, 0, 0
    a = num//25
    num = num%25
    b = num//10
    num = num%10
    c = num//5
    num = num%5
    
    d = num
    print(a,b,c,d)
    