# [0] 가중치 Table 설정
# D[] (Dijkstra Table) & v[] (visited Table) 생성
# 연결되어 있는 node 기준 미방문한 node 중 최소 거리(가중치) node로 이동
# [1] 미방문 노드 중 최소비용 노드 찾기(idx)
# [2] 모든 경로를 update, min(현재비용, 찾은 노드 경유 비용)
# 최소값 node마다 update 후 기준점으로 잡고 다음 node update, N-1 번 반복


# for _ in range(N-1) # N-1개 노드처리
#     # [1]
#     i_min(=0), mn <- INF(=N*10)
#     for j (0, N)
#         if v[j] == 0 and mn > D[j]
#             mn, i_min = D[j], j # i_min가 선택된 node가 된다
#     v[i_min]
#     # [2]
#     for j (N)
#         D[j] = min(D[j], D[i_min]+adj[i_min][j])


import sys
sys.stdin = open("input.txt", "r")

def dijkstra(s, e):
    # [0] D table, v[] 생성
    D = adj[s][::]
    v = [0] * N
    v[s] = 1

    # N-1개 노드에 대해서 반복처리
    for _ in range(N-1):
        # [1] 미방문 노드 중 기준노드(최소비용으로 연결가능한 노드) 찾기
        mn, i_min = INF, 0
        for j in range(N):
            if v[j]==0 and mn > D[j]:
                mn, i_min = D[j], j
        v[i_min] = 1 # 기준 노드 방문처리

        # [2] 모든 노드에 대해서 최소비용 갱신(D[])
        for j in range(N):
            # 현재 j까지 가는 비용, 기준노드를 경유해서 가는 비용 중 더 작은 값으로 갱신
            D[j] = min(D[j], D[i_min]+adj[i_min][j])

    return D[e]     # s -> e 까지의 최소 비용


INF = 50 * 10 # N의 최대값 * link의 최대값
T = int(input())

for tck in range(1, T+1):
    N, E = map(int, input().split())
    # 가중치 Table 기본 설정
    adj = [[INF]*N for _ in range(N)]
    for i in range(N):
        adj[i][i] = 0
    for _ in range(E): # 간선 개수만큼 입력
        s, e, w = map(int, input().split())
        adj[s][e] = w

    ans = dijkstra(0, N-1)
    print(f'#{tck} {ans}')