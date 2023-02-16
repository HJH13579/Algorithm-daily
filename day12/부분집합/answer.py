# 백트래킹 : 가능한 모든 경우를 실행 => 정답
# 표현 : 이진 Tree > 멀티 Tree

def dfs(n, sm):
    global ans
    # 종료조건 먼저 체크
    if n == N:
        if sm == K:
            ans += 1
        return

    # 하부함수 호출
    dfs(n + 1, sm + lst[n])  # 포함하는 경우
    dfs(n + 1, sm)  # 포함하지 않는 경우


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0
    dfs(0, 0)
    print(f'#{test_case} {ans}')