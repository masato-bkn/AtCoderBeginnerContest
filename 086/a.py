# A - Product
# https://atcoder.jp/contests/abc086/tasks/abc086_a

a,b = list(map(int,input().split()))

if (a*b)%2 == 1:
    print("Odd")

else:
    print("Even")
