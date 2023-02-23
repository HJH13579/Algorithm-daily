N = 5

arr = [[0]*N for _ in range(N)]

for i in range(-2, 3):
    for j in range(-2, 3):
        if 0 <= abs(i) + abs(j) <= 2 and 0 <= i < N and 0 <= j+1 < N:
            arr[i][j] = 1

print(arr)