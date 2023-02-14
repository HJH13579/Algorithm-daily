def dfs(s):
    for e in adj[s]:  # 나와 연결된
        if v[e] == 0:  # 방문하지 않은 노드
            v[e] = 1
            alst.append(e)
            dfs(e)


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    # [1] 연결리스트에 연결표시(append)
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)

    # adj 를 오름차순으로 정렬 필요!
    for i in range(1, V + 1):
        adj[i].sort()

    alst = []
    v = [0] * (V + 1)
    # 시작지점은 방문표시
    v[1] = 1
    alst.append(1)
    dfs(1)
    print(f'#{test_case}', *alst)