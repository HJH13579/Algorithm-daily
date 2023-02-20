import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tck in range(1, T + 1):
    N = int(input())
    C_lst = list(map(int, input().split()))

    cnt = 1

    lst = []

    i = 0

    while i < N - 1:
        if C_lst[i] + 1 == C_lst[i + 1]:
            cnt += 1

        else:
            cnt = 1

        lst.append(cnt)
        i += 1

    mx = 0

    for j in range(len(lst)):
        if mx < lst[j]:
            mx = lst[j]

    print(f'#{tck} {lst} {mx}')