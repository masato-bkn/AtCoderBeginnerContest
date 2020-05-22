# B - ROT N
# https://atcoder.jp/contests/abc146/tasks/abc146_b

N = int(input())
S = input()

tmp = ""
# ASCIIコード
for s in S:
    asc = ord(s) + N

    if asc > 90:
        asc = 64 + (asc - 90)

    tmp += chr(asc)

print(tmp)