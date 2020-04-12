# B - 1 21
# https://atcoder.jp/contests/abc086/tasks/abc086_b

import sys

a,b = input().split()

c = int(a + b)

i = 0

while i <= 10000:
    if (i * i) == c:
        print("Yes")
        sys.exit()

    i = i + 1

print("No")
