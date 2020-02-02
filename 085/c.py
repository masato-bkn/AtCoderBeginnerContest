# C - Otoshidama
# https://atcoder.jp/contests/abc085/tasks/abc085_c

N, Y = map(int,input().split())

# x 10000
# y 5000
# z 1000

for x in range(N+1):
    for y in range(N-x+1):
        z=N-(x+y)
        if 0<=z<=2000 and (x*10000)+(y*5000)+(z*1000) == Y:
            print(f"{str(x)} {str(y)} {str(z)}")
            exit()

print("-1 -1 -1")
