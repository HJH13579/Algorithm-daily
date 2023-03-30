def dfs(n, cnt, sm):
    global ans
    if ans <= cnt:
        return

    if n == N:
        ans = min(ans, cnt)
        return

    # 기존 풀이는 사고의 흐름대로
    # 다만, 시간 단축을 위한 추가적 상식
    # 기존 풀이는 dfs를 해보면 더 깊은, 더 절차를 거치는 것들 먼저 탐색하는 것을 알 수 있다.
    # 즉, 정답과 먼 풀이부터 탐색한다는 것
    # 시간 단축을 위해서는 답에 가까운 것부터 탐색하면 된다.
    # 순서만 바꿔주면 해결

    # 교체하지 않는 경우: 잔량>0 일때만 가능
    if sm > 0:
        dfs(n + 1, cnt, sm - 1)
    # 교체하는 경우: 항상 가능
    dfs(n + 1, cnt + 1, lst[n] - 1)


T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]
    ans = N  # 모든 정류장에서 교환하는것이 최악

    dfs(2, 0, lst[1] - 1)
    print(f'#{test_case} {ans}')