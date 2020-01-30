# C - Train Ticket
# https://atcoder.jp/contests/abc079/tasks/abc079_c

# A B C D の間に+,-を置く場合の数は
# 2*2*2 の８通りなので当てはまるパターンを表示すれば良い

a,b,c,d = map(int,list(input()))

if a + b + c + d == 7:
    print("a+b+c+d=7")
elif a - b - c - d == 7:
    print("a-b-c-d=7")
elif a + b - c + d == 7:
    print("a+b-c+d=7")
elif a - b + c - d == 7:
    print("a-b+c-d=7")
elif a + b - c - d == 7:
    print("a+b-c-d=7")
elif a - b - c + d == 7:
    print("a-b-c+d=7")
elif a - b + c + d == 7:
    print("a-b+c+d=7")
elif a + b + c - d == 7:
    print("a+b+c-d=7")
