# B - Some Sums
# https://atcoder.jp/contests/abc083/tasks/abc083_b

n,a,b = map(int,input().split())

ans = []

for i in range(int(n)+1):
    j = map(int,list(str(i)))
    tmp = 0
    for k in j:
        tmp += k

    if a <= tmp <= b:
        ans.append(i)

print(sum(ans))


# 別解
# N,A,B=map(int,input().split())
# print(sum(i for i in range(1,N+1) if A<=sum(map(int,str(i)))<=B))
