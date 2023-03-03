import sys
sys.stdin = open("input1.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    mx = 0

    for i in range(N):
        for j in range(M):
            sm = 0
            P = arr[i][j]
            sm += P

            for x in range(1, P+1):
                if i+x < N:
                    sm += arr[i+x][j]
                if i-x >= 0:
                    sm += arr[i-x][j]
                if j+x < M:
                    sm += arr[i][j+x]
                if j-x >= 0:
                    sm += arr[i][j-x]

            if mx < sm:
                mx = sm

    print(f'#{tck} {mx}')