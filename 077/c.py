# C - Snuke Festival
# https://atcoder.jp/contests/abc077/tasks/arc084_a

import bisect

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

a = sorted(a)
b = sorted(b)
c = sorted(c)

ans = 0

for x in b:
    aa = bisect.bisect_left(a,x)
    cc = len(c) - bisect.bisect_right(c,x)
    ans += aa + cc
print(ans)
