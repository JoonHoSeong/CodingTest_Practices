num = float(input())
grades = list(map(int,input().split(' ')))
grades = [i/max(grades)*100 for i in grades]
print(sum(grades)/num)