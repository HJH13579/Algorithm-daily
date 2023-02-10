# Runtime Error

import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N = int(input())

    griddle = [[0]*N for _ in range(N)]

    i = 0
    j = 0
    griddle[0][0] = 1

    while(1):

        cnt = 1

        for _ in range(N - cnt):
            if j + 1 == N or griddle[i][j + 1] != 0:
                continue
            else:
                griddle[i][j + 1] = griddle[i][j] + 1
                j += 1

        for _ in range(N - cnt):
            if i + 1 == N or griddle[i + 1][j] != 0:
                continue
            else:
                griddle[i + 1][j] = griddle[i][j] + 1
                i += 1

        for _ in range(N - cnt):
            if j == 0 or griddle[i][j - 1] != 0:
                continue
            else:
                griddle[i][j - 1] = griddle[i][j] + 1
                j -= 1

        for _ in range(N - cnt):
            if i == 0 or griddle[i - 1][j] != 0:
                continue
            else:
                griddle[i - 1][j] = griddle[i][j] + 1
                i -= 1

        cnt += 1

        if griddle[i + 1][j] != 0 and griddle[i - 1][j] != 0 and griddle[i][j + 1] != 0 and griddle[i][j - 1] != 0:
            break

    print(f'#{tck}')

    for lst in griddle:
        print(*lst)
