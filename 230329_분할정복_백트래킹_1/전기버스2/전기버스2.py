import sys
sys.stdin = open("s_input.txt", "r")

def dfs(cnt, n):
    return

T = int(input())

for tck in range(1, T+1):
    lst = list(map(int, input().split()))
    
    print(f'#{tck} {lst}')