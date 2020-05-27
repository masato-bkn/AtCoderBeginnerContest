# C - Train Ticket
# https://atcoder.jp/contests/abc079/tasks/abc079_c

# A B C D の間に+,-を置く場合の数は
# 2*2*2 の８通りなので当てはまるパターンを表示すれば良い

# a,b,c,d = map(int,list(input()))

# if a + b + c + d == 7:
#     print("a+b+c+d=7")
# elif a - b - c - d == 7:
#     print("a-b-c-d=7")
# elif a + b - c + d == 7:
#     print("a+b-c+d=7")
# elif a - b + c - d == 7:
#     print("a-b+c-d=7")
# elif a + b - c - d == 7:
#     print("a+b-c-d=7")
# elif a - b - c + d == 7:
#     print("a-b-c+d=7")
# elif a - b + c + d == 7:
#     print("a-b+c+d=7")
# elif a + b + c - d == 7:
#     print("a+b+c-d=7")

a,b,c,d = map(str,input())

for i in range(2**3):
    l = ["-","-","-"]
    for j in range(len(l)):
        if (i >> j) & 1:
            l[j] = "+"
    if eval(a+l[0]+b+l[1]+c+l[2]+d) == 7:
        print(a+l[0]+b+l[1]+c+l[2]+d+"=7")
        break
