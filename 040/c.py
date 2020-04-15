# C - 柱柱柱柱柱
# https://atcoder.jp/contests/abc040/tasks/abc040_c

# DP 動的計画法実装

# DP 配列全体を「DP の種類に応じた初期値」で初期化
# 初期条件を入力
# ループを回す
# テーブルから解を得て出力

N = int(input())
A = list(map(int, input().split()))

c = [0]*N

for i in range(1,N):
    c[i] = c[i-1] + abs(A[i]-A[i-1])

    if i > 1:
        c[i] = min(c[i],c[i-2] + abs(A[i]-A[i-2]))

print(c[-1])
