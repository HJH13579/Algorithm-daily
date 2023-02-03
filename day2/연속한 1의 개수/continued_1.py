import sys

sys.stdin = open("input1.txt", "r")

T = int(input())

for tck in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))

    count_lst = []

    cnt = 1
    i = 0

    while i < N - 1:

        if lst[i] == lst[i + 1] == 1:
            cnt += 1

        else:
            cnt = 1

        count_lst.append(cnt)

        i += 1

    mx = 0

    for j in range(len(count_lst)):
        if mx < count_lst[j]:
            mx = count_lst[j]

    print(f'#{tck} {mx}')