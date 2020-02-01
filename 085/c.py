# C - Otoshidama
# https://atcoder.jp/contests/abc085/tasks/abc085_c

N, Y = map(int,input().split())


# x 1000
# y 5000
# z 10000
for x in range(N+1):
    for y in range(N-x+1):
        z = N-x+y
        if (x*1000)+(y*5000)+(z*10000) == Y:
            print(f"{str(y)} {str(z)} {str(x)}")
            exit()

print("-1 -1 -1")
