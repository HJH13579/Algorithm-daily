N = 5

arr = [[0]*N for _ in range(N)]

for m in range(N):
    for n in range(N):
        for i in range(-2, 3):
            for j in range(-2, 3):
                if 0 <= abs(i) + abs(j) <= 2 and 0 <= i+m < N and 0 <= j+n < N:
                    arr[i+m][j+n] = 1

print(arr)