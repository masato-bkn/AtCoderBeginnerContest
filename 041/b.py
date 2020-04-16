# B - 直方体
# https://atcoder.jp/contests/abc041/tasks/abc041_b

A,B,C = [int(i) for i in input().split()]

# 体積
X = A * B * C

print(X % (pow(10,9) + 7))
