# B - Achieve the Goal
# https://atcoder.jp/contests/abc151/tasks/abc151_b

n,k,m =  map(int,input().split())
nums = map(int,input().split())
p = (m*n)-sum(nums)

if p <= k:
    if p < 0:
        print(0)
    else:
        print(p)
else:
    print(-1)