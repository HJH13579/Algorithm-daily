#0945269
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    mx = 0

    for i in range(N):
        for j in range(N):
            sm = arr[i][j]
            for ni, nj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                for x in range(1, P+1):
                    di, dj = i + ni*x, j + nj*x
                    if 0 <= di < N and 0 <= dj < N:
                        sm += arr[di][dj]

            if mx < sm:
                mx = sm

    print(f'#{test_case} {mx}')
