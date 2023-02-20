T = int(input())

for tck in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [[0] * N for _ in range(N)]   # NxN 정사각형

    for _ in range(M):
        i, j, m, n = map(int, input().split())

        for x in range(n):
            for y in range(m):
                arr[i + x][j + y] += 1  # 칸에 도장이 찍힐 때마다 +1 count

    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:  # 칠해진 칸, 즉 값이 0만 아니면 칠해진 칸으로 count
                cnt += 1        # 칠해진 칸 숫자 count(+1)

    print(f'#{tck} {cnt}')