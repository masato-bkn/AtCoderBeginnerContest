# B - Some Sums
# https://atcoder.jp/contests/abc083/tasks/abc083_b

N,A,B = list(map(int,input().split()))


tmp = []

for num in range(1,N+1):
    i = 0
    for n in list(str(num)):
        i += int(n)

    if A <= i <= B:
        tmp.append(num)

ans = 0

for t in tmp:
    ans += t

print(ans)   

