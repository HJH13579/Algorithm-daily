import sys
sys.stdin = open("s_input.txt", "r")

def changing(n, j, num):
    num_lst = list(str(num))
    num_lst[n], num_lst[j] = num_lst[j], num_lst[n]
    result = int(''.join(map(str, num_lst)))
    return result

def dfs(n, cnt, num):
    global ans
    if cnt == change_cnt:
        if n == N-1:
            ans = max(ans, num)
            return

    else:
        for j in range(n+1, N):
            dfs(n+1, cnt+1, changing(n, j, num))

        dfs(n+1, cnt, num)

T = int(input())

for tck in range(1, T+1):
    num_plate, change_cnt = map(int, input().split())

    N = len(str(num_plate))
    ans = 0

    dfs(0, 0, num_plate)

    print(f'#{tck} {ans}')