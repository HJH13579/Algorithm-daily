import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    alst = []

    for i in range(1, N-1):
        for j in range(1, N-1):
            for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (-1, 0), (0, 1), (1, 0)):
                if arr[i][j] <= arr[i+di][j+dj]:
                    break
            else:
                alst.append(arr[i][j])

    if len(alst) == 1:
        ans = -1
    else:
        ans = max(alst) - min(alst)

    print(f'#{test_case} {ans}')