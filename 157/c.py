# C - Guess The Number
# https://atcoder.jp/contests/abc157/tasks/abc157_c

N,M = list(map(int,input().split()))

digit_num_list = [list(map(int, input().split())) for i in range(0,M)]

# 最小数、最大数を作る。
min = ["1"]
for n in range(1,N):
    min.append("0")
min = int("".join(min))

max = []
for n in range(0,N):
    max.append("9")
max = int("".join(max))

# print(min)
# print(max)

# 求める整数
ans = ["0"]*N
# print(len(ans))


# M桁目まで検証すればよい。
for i in range(min,max):
    cnt = 0
    for digit_num in digit_num_list:

        # # print("=========")
        # # print(digit_num)
        # # print(str(i))
        # # print(digit_num[0])
        # # print(str(i)[digit_num[0]]-1)
        # # print("=========")

        # print("=========")
        # print(int(str(i)[digit_num[0]-1]))
        # print(digit_num[1])
        # print(i)
        # print("=========")

        if int(str(i)[digit_num[0]-1]) == digit_num[1]:
            ans[digit_num[0]-1] = str(digit_num[1])
            print(ans)
            cnt += 1
        else:
            break

        print("".join(ans))
        exit()

    if cnt == N:
        print("".join(ans))
        exit()

print(-1)

