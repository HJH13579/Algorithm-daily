import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N = float(input())

    M = round(N ** (1/3), 2)

    if int(M) == M:
        ans = int(M)
    else:
        ans = -1

    print(f'#{tck} {ans}')