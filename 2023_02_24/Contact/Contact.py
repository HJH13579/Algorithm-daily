import sys
sys.stdin = open("input.txt", "r")

def contact(n, v):
    visited[n] = v  # 방문 시 몇 번째 단계의 방문인지 기록

    for e in adj[n]:
        if visited[e] == 0 or visited[e] > v+1: # BFS 재귀 알고리즘은 결국 한 쪽 진행이 끝난 후 다음으로 넘어간다.
                                                # 방문한 적이 없는 것만 체크하면 좀 더 긴 경로를 통해 앞서 방문하게 된 경로가 먼저 방문 마크를 남기고,
                                                # 뒤이어 방문하게 될 더 짧은 경로는 방문 마크 때문에 무시 당한다. 하지만 문제는 확산 속도가 동시에 진행되기에 짧은 진행 속도 기준이 맞다.
                                                # 결국 우리는 아예 방문한 적이 있거나, 만약 방문했었어도 뒤이어 검사할 경로가 기존 방문보다 더 단계가 적은지까지 검사해야한다.
            contact(e, v+1) # 단계 +1

for tck in range(1, 11):
    L, s = map(int, input().split())
    lst = list(map(int, input().split()))

    adj = [[] for _ in range(101)]  # 부여 번호가 1이상 100이하
    visited = [0]*101   # visited list는 단순히 방문여부만 나타내는 것이 아닌, 몇 단계에서 방문했는 지 기록하는 리스트

    for i in range(0, L, 2):
        adj[lst[i]].append(lst[i+1])

    contact(s, 1)

    idx_mx = 0
    for x in range(len(visited)):
        if visited[idx_mx] <= visited[x]:
            idx_mx = x

    print(f'#{tck} {idx_mx}')