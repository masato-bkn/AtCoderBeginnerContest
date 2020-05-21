# C - Welcome to AtCoder
# https://atcoder.jp/contests/abc151/tasks/abc151_c

n,m = map(int,input().split())

# 問題数分配列を作成 -> 正解判定用の関数
ac = [False] * n
wa = [0] * n

# まずはテーブルを作成する
for i in range(m):
    p, s = input().split()
    p = int(p) - 1

    if s == "AC":
        # 正解したことのある問題か確認
        ac[p] = True
    else:
        if ac[p] == False:
            wa[p] += 1

ac_cnt = 0
wa_cnt = 0

for i in range(n):
    if ac[i] == True:
        ac_cnt += 1
        wa_cnt += wa[i]

print(ac_cnt,wa_cnt)