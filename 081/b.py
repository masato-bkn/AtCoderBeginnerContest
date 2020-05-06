# B - Shift only
# https://atcoder.jp/contests/abc081/tasks/abc081_b

N = input()
nums = list(map(int,input().split()))

count= 0
while all([num % 2 == 0 for num in nums]): #リスト内包表記の[]、あってもなくてもいいみたい。
    nums = [(num/2) for num in nums]
    count +=  1

print(count)
