# A - 和風いろはちゃんイージー / Iroha and Haiku (ABC Edition)
# https://atcoder.jp/contests/abc042/tasks/abc042_a

nums = list(map(int,input().split()))

for i in [5,7,5]:
    if i in nums:
        nums.remove(i)
    else:
        print("NO")
        exit()

if len(nums) == 0:
    print("YES")
else:
    print("NO")