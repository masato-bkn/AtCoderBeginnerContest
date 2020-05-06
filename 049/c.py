# coding: utf-8
# Your code here!

# 商品の総数
N = int(input())

# 0:食料品
groceries = []
# 1:書籍
books = []
# 2:衣類
wear = []
# 3:その他
anothers = []

# 購入商品の内訳

for i in range(N):
    v,p = list(map(int,input().split()))
    
    if v == 0:
        groceries.append(p)
    elif v == 1:
        books.append(p)
    elif v == 2:
        wear.append(p)
    elif v == 3:
        anothers.append(p)
    
# ポイント(食料品/書籍/衣類/その他の順)
point = [5,3,2,1]

# 合計ポイント
total_point = 0

for i,item_type in enumerate([groceries,books,wear,anothers]):
     
    total_price_by_type = 0

    for item in item_type:
        total_price_by_type += item
    # ポイントを計算。 => 100円ごとに商品ごとに決まったポイントを付与(100円未満は切捨て)
    total_point += (total_price_by_type//100)*point[i]

print(total_point)