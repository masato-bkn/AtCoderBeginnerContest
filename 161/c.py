# C - Replacing Integer
# https://atcoder.jp/contests/abc161/tasks/abc161_c

N,K = list(map(int,input().split()))

# while 1 != 0:
#     if N - K >= 0:
#         N = abs(N - K)
#     else:
#         print(N)
#         exit()

# Nの数が大きすぎるとタイムアウトする
# 求める最小値がN/Kの余りかK-(N/K)の余りであることを利用して解く。

# 7%3 -> 1
# 3-(7%3) -> 2

print(min((N%K),K-(N%K)))