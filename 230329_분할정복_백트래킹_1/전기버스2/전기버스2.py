import sys
sys.stdin = open("s_input.txt", "r")

def dfs(cnt, n):
    if n == N-2:
        return cnt
    else:
        for idx in range(1, M[n]+1):
            dfs(cnt+1, n+idx)

T = int(input())

for tck in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst[0]
    M = [lst[i] for i in range(1, N)]

    ans = dfs(0, 0)
    
    print(f'#{tck} {ans}')