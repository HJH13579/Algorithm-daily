import sys

sys.stdin = open("input.txt", "r")

def power(n, m):
    if m == 1:
        return n
    return n * power(n, m - 1)

for tck in range(1, 11):
    _ = int(input())
    N, M = map(int, input().split())

    print(f'#{tck}', power(N, M))