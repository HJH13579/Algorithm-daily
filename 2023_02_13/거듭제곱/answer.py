# 재귀함수
# [1] 종료조건
# [2] 단위작업

# 재귀 함수 풀이
def power(n, m):
    if m == 1:
        return n
    return n * power(n, m - 1)


T = 10
for test_case in range(1, T + 1):
    _ = input()
    N, M = map(int, input().split())
    ans = power(N, M)
    print(f'#{test_case} {ans}')


# DFS 풀이
def dfs(n, m, mul):
    if m == M:
        return mul
    return dfs(n, m + 1, mul * n)


T = 10
for test_case in range(1, T + 1):
    _ = input()
    N, M = map(int, input().split())
    ans = dfs(N, 0, 1)
    print(f'#{test_case} {ans}')