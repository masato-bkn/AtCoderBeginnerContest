# C - Welcome to AtCoder
# https://atcoder.jp/contests/abc151/tasks/abc151_c

n,m = map(int,input().split())

# 2 5
# 1 WA
# 1 AC
# 2 WA
# 2 AC
# 2 WA
# 2 2

# 提出問題数の分だけ配列を作る
ac = [False] * n
wa = [0] * n 

# ================
# ac F T .....
# wa 1 2 .....
# ================

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
    # Tの数をカウント。
    if ac[i] == True:
        ac_cnt += 1
        wa_cnt += wa[i]

print(ac_cnt,wa_cnt)