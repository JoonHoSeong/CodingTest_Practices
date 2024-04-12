sub = []
for i in range(28) :
    sub.append(int(input()))
total = [i+1 for i in range(30)]
for i in total :
    if i not in sub :
        print(i)