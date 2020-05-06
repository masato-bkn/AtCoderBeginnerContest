# C - Rally
# https://atcoder.jp/contests/abc156/tasks/abc156_c


p = int(input())
nums = list(map(int,input().split()))

total = 0


for num in nums:
    total += (num - p) ** 2

print(total)

# 取り合え合うここまで、c解説読んでもわからんやつ多い胃からコスパ悪い。