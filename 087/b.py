# B - Coins
# https://atcoder.jp/contests/abc087/tasks/abc087_b

# A 500円玉
# B 100円 
# C 50円

a,b,c,x = map(int,[input() for i in range(4)])

ans = 0

for  i in range(a+1):
    for  j in range(b+1):
        for k in range(c+1):
            tmp = (500 * i) + (100 * j) + (50 * k)
            if tmp == x:
                ans += 1

print(ans)