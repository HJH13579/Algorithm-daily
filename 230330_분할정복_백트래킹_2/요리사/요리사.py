import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    idx_lst = [idx for idx in range(1, N+1)]

    print(f'#{tck} {ans}')