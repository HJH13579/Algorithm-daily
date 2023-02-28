import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N = int(input())
    M = N // 2

    arr = [list(map(int, input())) for _ in range(N)]

    sm = 0
    for i in range(N):
        for j in range(N):
            if -M <= abs(i - M) + abs(j - M) <= M:
                sm += arr[i][j]

    print(f'#{tck} {sm}')