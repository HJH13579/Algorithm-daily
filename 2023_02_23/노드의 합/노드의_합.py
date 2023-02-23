import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N, M, L = map(int, input().split())

    ch = [0]*(N+1)

    for _ in range(M):
        idx, val = map(int, input().split())
        ch[idx] = val

    i = N
    while i > 0:
        if i * 2 == N:
            ch[i] = ch[i*2]
        elif i * 2 + 1 <= N:
            ch[i] = ch[i*2] + ch[i*2+1]

        i -= 1

    print(f'#{tck} {ch[L]}')