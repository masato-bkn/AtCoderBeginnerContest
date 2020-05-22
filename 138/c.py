# C - Alchemist
# https://atcoder.jp/contests/abc138/tasks/abc138_c

n = int(input())
v = sorted(list(map(int,input().split())))

tmp = 0

for i in range(n):
    if i == 0:
        tmp = v[i]
    else:
        tmp = (tmp + v[i])/2

print(tmp)