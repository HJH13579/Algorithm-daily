import sys
from collections import deque
sys.stdin = open("s_input.txt", "r")

def bfs(arr, start):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = 1
    ans = []

    while queue:
        node = queue.popleft()
        ans.append(node)
        for i in arr[node]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
    return ans

T = int(input())

for tck in range(1, T+1):
    V, E = map(int, input().split())

    # 인접행렬
    adjL = [[] for _ in range(V + 1)]

    # 방향이 없는 경우
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adjL[n1].append(n2)
        adjL[n2].append(n1)

    # 중복방지
    visited = [0] * (V+1)

    answer = bfs(adjL, 1)

    print(f'#{tck}', *answer)
