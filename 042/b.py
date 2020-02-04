# B - 文字列大好きいろはちゃんイージー / Iroha Loves Strings (ABC Edition)
# https://atcoder.jp/contests/abc042/tasks/abc042_b

n,l= map(int,input().split())
 
words = []
 
[words.append(input()) for i in range(n)]
 
print("".join(sorted(words)))