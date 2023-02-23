import sys
sys.stdin = open("sample_input.txt", "r")

def movement(r, c):
    visited[r][c] = 1
    if arr[r][c] == 1:
        movement(r, c+1)
        movement(r, c-1)



T = int(input())

for tck in range(1, T+1):
    N, M, R, C, L = map(int, input().split())

    arr = [[0]*(M+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(M+2)]
    visited = [[0]*(M+2) for _ in range(N+2)]

    # visited ==0 & arr[i][j] != 0 & 지하터널이 이어져있어야한다!

    print(f'#{tck} {arr}')