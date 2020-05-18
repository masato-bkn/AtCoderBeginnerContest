# C - Snack
# https://atcoder.jp/contests/abc148/tasks/abc148_c

import fractions

# 最小公倍数を求める問題
A,B = map(int,input().split())

print((A * B) // fractions.gcd(A, B))