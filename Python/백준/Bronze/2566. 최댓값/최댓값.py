max_val = -1
row, col = 0, 0
for i in range(9) :
    temp = list(map(int, input().split()))
    temp_max = max(temp)
    if max_val < temp_max :
        max_val = temp_max
        row = i+1
        col = temp.index(temp_max) + 1
print(max_val)
print(row,col)