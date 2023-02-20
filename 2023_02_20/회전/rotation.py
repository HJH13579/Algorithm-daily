import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for tck in range(1, T+1):
    N, M = map(int, input().split())

    lst = list(map(int, input().split()))

    n = M % N

    ans = lst[n]

    print(f'#{tck} {ans}')


