# C - Traveling Salesman around Lake
# https://atcoder.jp/contests/abc160/tasks/abc160_c

# 各家において、時計回りか反時計回りのどちらで移動した方が良いかチェックする。

K,N = list(map(int,input().split()))
A = list(map(int,input().split()))

result = A[0] - A[N - 1] + K
for i in range(N - 1):
    result = max(result, A[i + 1] - A[i])
print(K - result)

# 1個所だけ通らないところがあり、そこが最大となると個所を求めれば良い。
