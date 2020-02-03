# C - Traveling
# https://atcoder.jp/contests/abc086/tasks/arc089_a

# 入力
# 2
# 3 1 2
# 6 1 1

N = int(input())

T,X,Y = 0,0,0

cnt = 0

for n in range(N):
    t,x,y = map(int,input().split())

    dt = t-T 
    dx = x-X
    dy = y-Y

    if dt < abs(dx) + abs(dy) or (dx + dy) % 2 != (dt % 2):
        print("No")
        exit()
    T,X,Y = t,x,y


print("Yes")
