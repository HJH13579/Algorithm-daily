V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접행렬
adjM = [[0]*(V+1) for _ in range(V+1)]
# 인접리스트
adjL = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = arr[2*i], arr[2*i+1]

    # 방향이 없는 경우
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1

    adjL[n1].append(n2)
    adjL[n2].append(n1)

print(adjM)
print(adjL)