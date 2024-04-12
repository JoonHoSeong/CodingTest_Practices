row ,col = map(int, input().split(' '))
arr1 = []
arr2 = []
for i in range(row *2) :
    if i < row :
        arr1.extend(list(map(int, input().split(' '))))
    else :
        arr2.extend(list(map(int, input().split(' '))))
for r in range(row) :
    for c in range(col) :
        print(arr1[r*col+c]+arr2[r*col+c],end= ' ')
    print()