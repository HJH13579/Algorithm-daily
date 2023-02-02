import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N = int(input())
    lst = list(map(int, input()))

    # [1] 빈도수 배열에 빈도 표시

    counts_lst = [0] * 10

    for i in range(N):
        counts_lst[lst[i]] += 1

    mx = 0

    for i in range(10):
        if mx < counts_lst[i]:
            mx = counts_lst[i]

    mx_num = 0

    for j in range(10):
        if mx == counts_lst[j]:
            mx_num = j

    print(f'#{tck} {mx_num} {mx} {counts_lst}')