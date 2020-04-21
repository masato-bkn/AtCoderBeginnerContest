# C - Tax Increase
# https://atcoder.jp/contests/abc158/tasks/abc158_c

A,B = map(int,input().split())

i = 0

for i in range(2000):
    if int(i * 0.08) == A and int(i * 0.1) == B:
        print(i)
        exit()
print(-1)