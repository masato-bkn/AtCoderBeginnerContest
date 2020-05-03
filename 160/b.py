# B - Golden Coins
# https://atcoder.jp/contests/abc160/tasks/abc160_b

# 所持金
X = int(input())

# 嬉しさ(= 残金計算時にも使用)
happy = 0

# 500円玉,5円玉の最大両替枚数
max_five_hundred = X//500
max_five = (X-(max_five_hundred*500))//5

# 各硬化の枚数をもとに嬉しさを算出
print((max_five_hundred*1000)+(max_five*5))