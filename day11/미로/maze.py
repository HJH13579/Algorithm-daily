import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T + 1):
    N = int(input())

    # 전면 padding
    mazeArr = [[1] * (N+2)] + [[1] + list(map(int, input())) + [1] for _ in range(N)] + [[1] * (N+2)]

    # 상하좌우(좌, 우, 하, 상)
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]

    # 시작점 찾기
    ni = 0
    nj = 0

    for i in range(N+2):
        for j in range(N+2):
            if mazeArr[i][j] == 2:
                ni = i
                nj = j

    # 백트래킹


    print(f'#{tck} {ni} {nj}')