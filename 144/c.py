# C - Walk on Multiplication Table
# https://atcoder.jp/contests/abc144/tasks/abc144_c

import math

n = int(input())
sqr = int(math.sqrt(n)) + 1
for i in range(sqr, 0, -1):
         if (n % i) == 0:
            # iがわかれば自ずと、jも算出できる。
            print(i + (n//i) - 2)
            exit()
