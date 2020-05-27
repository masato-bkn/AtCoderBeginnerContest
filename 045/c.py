# C - たくさんの数式
# https://atcoder.jp/contests/abc045/tasks/arc061_a

s = input()
n = len(s)

ans = 0

# 選択肢はn*1桁存在する。

for bit in range(1 << (n-1)):
    # bit -> 0123

    f=s[0]

    # range(n-1) -> 3桁の数字の場合、+が入る場所は2つになるから
    for i in range(n-1):
        if bit & (i << i):
            f += "+"
        f += s[i + 1]
    
    ans += sum(map(int,f.split("+")))

print(ans)