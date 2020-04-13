# C - こだわり者いろはちゃん
# https://atcoder.jp/contests/abc042/tasks/arc058_a

# 入力 1
# 1000 8
# 1 3 4 5 6 7 8 9

N,K = input().split()
D = input().split()

# Nの各桁をみて、嫌いな数字が入っていないかチェック
# 嫌いな数字が入っていたら、その桁をインクリメントして、整数(N)を再生性する。
# これを嫌いな数字がなくなるまで繰り返す。

nums = list(N) # 各桁

i = 1

# 嫌いな数字が入っていたら、その桁をインクリメントして、整数(N)を再生性する。
while i != 0:
    tmp = []
    j = 0
    for num in nums :
        if num in D:
            tmp.append(str(int(num) + 1))
            j = 1
        else :
            tmp.append(num)
    
    # 嫌いな数字があったか判定
    if j == 1:
        i = 1
        nums = "".join(tmp)
    else :
        print("".join(tmp))
        exit()

# テストケース
