# B - ROT N
# https://atcoder.jp/contests/abc146/tasks/abc146_b

N = int(input())
S = input()

tmp = ""
# ASCIIコード A=65/Z=90
for s in S:
    asc = ord(s) + N

    if asc > 90:
        unicode_point = 64 + (unicode_point - 90)

    tmp += chr(asc)

print(tmp)