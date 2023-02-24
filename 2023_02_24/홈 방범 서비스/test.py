N = 5
max_K = 3

for x in range(N):
    for y in range(N):
        arr_ser = [[0] * N for _ in range(N)]
        for i in range(-(max_K - 1), max_K):
            for j in range(-(max_K - 1), max_K):
                if 0 <= abs(i) + abs(j) <= (max_K - 1) and 0 <= i + x < N and 0 <= j + y < N:
                    arr_ser[i + x][j + y] = 1

        print(arr_ser)