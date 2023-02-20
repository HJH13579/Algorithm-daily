import sys
sys.stdin = open("input.txt", "r")

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    alst = []

    # 방향이 바뀔 때마다 저장
    ci, cj = 0, 0
    v[ci][cj] = 1
    dr = arr[0][0]
    alst.append(dr)

    while True:
        ni, nj = ci+di[dr], cj+dj[dr]
        # 범위 내이고 미방문이면 방문
        if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
            ci, cj = ni, nj
            v[ni][nj]=1
            if dr != arr[ni][nj]:
                dr = arr[ni][nj]
                alst.append(dr)
        else:
            break

    print(f'#{tc}', *alst)