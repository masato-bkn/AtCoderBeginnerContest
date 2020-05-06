# B - Coins
# https://atcoder.jp/contests/abc087/tasks/abc087_b

# A 500円玉
# B 100円 
# C 50円
A = int(input())
B = int(input())
C = int(input())
X = int(input())

i = 0

for a in range(A+1):
    if (a * 500) == X:
        i += 1
        break

    for b in range(B+1):
        if (a * 500) + (b * 100) == X:
            i += 1
            break

        for c in range(C+1):
            if (a * 500) + (b * 100) + (c * 50)== X:
                i += 1
                break

print(i)