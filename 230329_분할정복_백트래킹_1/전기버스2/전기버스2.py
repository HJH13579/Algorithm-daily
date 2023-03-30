import sys
sys.stdin = open("s_input.txt", "r")

def dfs(n, cnt, charge):
    global ans

    if ans <= cnt:
        return

    if n == N:
        ans = min(ans, cnt)
        return

    else:
        # 다음 정류장으로 갈 때
        # 충전을 안하고 charge를 1 소모, cnt X
        # 단 charge가 0이 되기 전까지
        if charge > 0:
            dfs(n+1, cnt, charge-1)
        # 충전, cnt +1
        # 충전은 언제든지 해도 되므로, else 없이 진행
        dfs(n+1, cnt+1, lst[n]-1)

T = int(input())

for tck in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst[0]

    ans = N

    dfs(1, 0, lst[1])

    print(f'#{tck} {ans}')