# B - Card Game for Two
# https://abc088.contest.atcoder.jp/tasks/abc088_b

n = int(input())
a = sorted(list(map(int,input().split())), reverse=True)

print(sum(a[::2]) - sum(a[1::2]))
