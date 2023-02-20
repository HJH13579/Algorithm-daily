import sys

sys.stdin = open("input1.txt", "r")

T = int(input())

for tck in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))

    count_lst = []

    cnt = 0

    for i in range(N - 1):

        if lst[i] == 0 and lst[i + 1] == 1:
            cnt = 1

        if lst[i] == 1 and lst[i + 1] == 1:
            cnt += 1

        if lst[i] == 1 and lst[i + 1] == 0:
            cnt = 0

        count_lst.append(cnt)

    mx = 0

    for j in range(len(count_lst)):
        if mx < count_lst[j]:
            mx = count_lst[j]

    print(f'#{tck} {mx}')