ball_num, c_num = map(int, input().split(' '))
balls = [str(i+1) for i in range(ball_num)]
for i in range(c_num):
    one, two = map(int,input().split(' '))
    temp = balls[one-1]
    balls[one-1] = balls[two-1]
    balls[two-1] = temp
print(' '.join(balls))