s = input()
alpha_list = [0 for _ in range(ord('a'), ord('z')+1)]
for i in s:
    temp = ord('a')
    alpha_list[ord(i)-temp] += 1
for i in alpha_list :
    print(i, end=' ')