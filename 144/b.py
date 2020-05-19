# B - 81
# https://atcoder.jp/contests/abc144/tasks/abc144_b

n = int(input())

multi_table = []

for i in range(1,10):
    for j in range(1,10):
        multi_table.append(i*j)

if n in multi_table:
    print("Yes")
else :
    print("No")    
