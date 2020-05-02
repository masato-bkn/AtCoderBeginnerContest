# B - Popular Vote
# https://atcoder.jp/contests/abc161/tasks/abc161_bß

# N 商品の種類数
# M 選択したい商品数
# votes 各商品ごとの投票数
N,M = list(map(int,input().split()))
votes = list(map(int,input().split()))

# 総投票数
total_vote = 0

# 総投票数算出
for vote in votes:
    total_vote += vote

# 購入できる商品数
i = 0

for vote in votes:
    # 得票数が総投票数の 1/4M 以上であれば商品を選択
    if vote >= total_vote*(1/(4*M)):
        i += 1

# 商品をM個購入できる場合
if i >= M:
    print("Yes")
else:
    print("No")