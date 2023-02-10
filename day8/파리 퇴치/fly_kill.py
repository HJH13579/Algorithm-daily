import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T + 1):

    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    num_lst = []

    sum_dead_fly = 0

    for x in range(N - M + 1):
        for y in range(N - M + 1):

            sum_dead_fly = 0
            for i in range(M):
                for j in range(M):
                    sum_dead_fly += arr[x + i][y + j]

            num_lst.append(sum_dead_fly)

    mx = 0
    for k in num_lst:
        if mx < k:
            mx = k

    print(f'#{tck} {mx}')