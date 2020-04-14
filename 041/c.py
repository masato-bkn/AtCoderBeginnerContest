# C - 背の順
# https://atcoder.jp/contests/abc041/tasks/abc041_c

N = int(input())
A = [int(i) for i in input().split()]

tmp = list(enumerate(A, start=1)) 
tmp.sort(key=lambda x:x[1], reverse=True)

for t in tmp:
    print(t[0])

# forで辞書を作ると遅くなる。
