# C - Traveling
# https://atcoder.jp/contests/abc086/tasks/arc089_a

# dt = ti+1 −ti
# dist = abs(xi+1 − xi)+abs(yi+1 − yi)

# キーポイント: パリティ
# x + y は毎秒ごとに必ず偶奇が入れ替わる。

n = int(input())

T = 0
X = 0
Y = 0

cnt = 0

for i in range(n):
    t,x,y= map(int,input().split())

    dist = abs(x-X) + abs(y-Y)
    dt = (t-T)

    # dist と dt の偶奇は一致する必要あり
    if dist <= dt and dist%2 == dt%2:
        cnt += 1
    T,X,Y = t,x,y
print("Yes" if cnt == n else "No")
    
