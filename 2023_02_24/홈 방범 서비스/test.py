N = 5

arr = [[0]*N for _ in range(N)]

for i in range(-2, 3):
    for j in range(-2, 3):
        if 0 <= abs(i) + abs(j) <= 2:
            arr[i+2][j+2] = 1

print(arr)