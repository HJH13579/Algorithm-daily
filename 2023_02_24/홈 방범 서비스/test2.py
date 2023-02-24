N = 7

arr = [[0]*N for _ in range(N)]

for i in range(-3, 4):
    for j in range(-3, 4):
        if 0 <= abs(i) + abs(j) <= 3 and 0 <= i+1 < N and 0 <= j+1 < N:
            arr[i+1][j+1] = 1

print(arr)